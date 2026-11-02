import flet as ft

def main(page: ft.Page):
    page.title = "Volleyball Pro"
    page.bgcolor = "#0f172a"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    beep = ft.Audio(src="beep.mp3", autoplay=False)
    page.overlay.append(beep)

    team_a = ft.TextField(value="TEAM A", width=130, text_align=ft.TextAlign.CENTER)
    team_b = ft.TextField(value="TEAM B", width=130, text_align=ft.TextAlign.CENTER)

    score_a = ft.Text("0", size=90, color="#38bdf8", weight="bold", animate_scale=ft.Animation(300, "bounceOut"))
    score_b = ft.Text("0", size=90, color="#fb7185", weight="bold", animate_scale=ft.Animation(300, "bounceOut"))
    
    sets_a = ft.Text("Sets: 0", color="white")
    sets_b = ft.Text("Sets: 0", color="white")
    info = ft.Text("First to 25, Win by 2 | Best of 3", color="grey", size=11)
    history = ft.Column([], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    sa = 0; sb = 0; set_a = 0; set_b = 0

    def play_beep():
        try: beep.play()
        except: pass

    def win_check():
        nonlocal sa, sb, set_a, set_b
        if (sa >= 25 or sb >= 25) and abs(sa - sb) >= 2:
            history.controls.append(ft.Text(f"{team_a.value} {sa}-{sb} {team_b.value}", color="white"))
            if sa > sb: set_a += 1
            else: set_b += 1
            sets_a.value = f"Sets: {set_a}"; sets_b.value = f"Sets: {set_b}"
            sa = 0; sb = 0; score_a.value = "0"; score_b.value = "0"
            if set_a == 2 or set_b == 2:
                winner = team_a.value if set_a == 2 else team_b.value
                info.value = f"🏆 {winner} WON!"; info.color = "yellow"; info.size = 16
            page.update()

    def add_a(e): 
        nonlocal sa; sa+=1; score_a.value=str(sa); play_beep(); win_check(); page.update()
    def sub_a(e):
        nonlocal sa
        if sa>0: sa-=1; score_a.value=str(sa); page.update()
    def add_b(e):
        nonlocal sb; sb+=1; score_b.value=str(sb); play_beep(); win_check(); page.update()
    def sub_b(e):
        nonlocal sb
        if sb>0: sb-=1; score_b.value=str(sb); page.update()
    def reset(e):
        nonlocal sa, sb, set_a, set_b
        sa=0; sb=0; set_a=0; set_b=0
        score_a.value="0"; score_b.value="0"; sets_a.value="Sets: 0"; sets_b.value="Sets: 0"
        history.controls.clear(); info.value="First to 25, Win by 2 | Best of 3"; info.color="grey"
        page.update()

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("VOLLEYBALL PRO", color="white", weight="bold", size=24),
                info,
                ft.Row([team_a, ft.Text("VS", color="white"), team_b], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Column([sets_a, score_a, ft.Row([ft.ElevatedButton("-", on_click=sub_a), ft.ElevatedButton("+", on_click=add_a)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Text(":", color="white", size=40),
                    ft.Column([sets_b, score_b, ft.Row([ft.ElevatedButton("-", on_click=sub_b), ft.ElevatedButton("+", on_click=add_b)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ], alignment=ft.MainAxisAlignment.CENTER),
                history,
                ft.ElevatedButton("NEW MATCH", bgcolor="red", color="white", on_click=reset)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=18),
            gradient=ft.LinearGradient(begin=ft.alignment.top_left, end=ft.alignment.bottom_right, colors=["#0f172a", "#312e81"]),
            padding=20, border_radius=20
        )
    )

ft.app(target=main)

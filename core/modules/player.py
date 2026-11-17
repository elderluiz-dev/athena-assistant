import subprocess

def is_spotify_available():
    result = subprocess.run(
        ["playerctl", "--player=spotify", "status"],
        capture_output=True,
        text=True
    )

    return result.returncode == 0

def open_spotify():
    if not is_spotify_available():
        subprocess.Popen(
            ["spotify"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
    
        return {
        "type": "player",
        "success": True,
        "message": "Spotify iniciado."
        }

    else:
        return {
        "type": "player",
        "success": False,
        "message": "Spotify já está aberto."
        }



def music_player(action):
    if is_spotify_available():
        result = subprocess.run(
            ["playerctl", "--player=spotify", action],
            capture_output=True,
            text=True
        )

        return {
            "type": "player",
            "success": result.returncode == 0,
            "message": result.stderr.strip()
        }

    

    else:
        choose = input("Abrir spotify? (S/N): ")
        if choose.lower() == "s":
            subprocess.Popen(
                ["spotify"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
            
            return {
            "type": "player",
            "success": True,
            "message": "Spotify iniciado."
            }



    return {
        "type": "player",
        "success": False,
        "message": "Operação cancelada."
    }

    
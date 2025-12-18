from pyscript import Element

def show_club_info():
    box = Element("club-info-container").element

    box.innerHTML = """
    <div style="display:flex; font-family:Glacial Indifference, sans-serif;">

        <div style="width:50%;">
            <div style="color:#6a00ff; font-size:36px; font-weight:bold;">
                Description:
            </div>
            <div style="font-size:38px; font-weight:bold;">
                A friendly space<br>
                to jam and learn<br>
                new chords!
            </div>
        </div>

        <div style="width:50%;">
            <div style="color:#6a00ff; font-size:32px; font-weight:bold;">
                Time:
            </div>
            <div style="font-size:32px; font-weight:bold;">
                Every Monday,<br>
                2:00 to 3:00 PM
            </div>

            <div style="color:#6a00ff; font-size:32px; font-weight:bold; margin-top:20px;">
                Location:
            </div>
            <div style="font-size:32px; font-weight:bold;">
                Room 221
            </div>
        </div>

    </div>
    """

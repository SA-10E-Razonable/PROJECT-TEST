from pyscript import display, document, when

club_info = {
    "guitar": {
        "description": "A friendly space to jam and learn new chords!",
        "meeting_time": "Every Monday, 2:00 to 3:00 PM",
        "location": "Room 221"
    }
}

@when("click", "#show-info-btn")
def show_club_info(e=None):
    container = document.getElementById("club-info-container")
    container.innerHTML = ""

    info = club_info["guitar"]

    output = f"""
        <div class="row">
            <div class="col-md-6">
                <div class="category-title" style="color:#FF5733;">Description:</div>
                <div class="club-description" style="color:#1C1C1C;">
                    {info['description']}
                </div>
            </div>

            <div class="col-md-6">
                <div class="category-title" style="color:#FF5733;">Time:</div>
                <div class="club-time" style="color:#1C1C1C;">
                    {info['meeting_time']}
                </div>

                <div class="category-title mt-3" style="color:#FF5733;">Location:</div>
                <div class="club-location" style="color:#1C1C1C;">
                    {info['location']}
                </div>
            </div>
        </div>
    """
    display(output, target="club-info-container")




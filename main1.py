<py-script>
from js import document

def show_club_info(event=None):
    container = document.getElementById("club-info-container")

    container.innerHTML = """
        <div class="row">
            <div class="col-md-6">
                <div class="category-title">Description:</div>
                <div class="club-description">
                    A friendly space to jam and learn new chords!
                </div>
            </div>

            <div class="col-md-6">
                <div class="category-title">Time:</div>
                <div class="club-time">
                    Every Monday,<br>2:00 to 3:00 PM
                </div>

                <div class="category-title mt-3">Location:</div>
                <div class="club-location">
                    Room 221
                </div>
            </div>
        </div>
    """
</py-script>






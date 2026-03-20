#checks if no progress has been made in whatever activity/exercise has been selected before a session begins
def start_check(user_id):
    #check if user has made any progress in the selected activity/exercise
    #if no progress, the app will display the no_progress_data for its respected activity/exercise section
    #if progress has been made, the app will generate its own data for the activity/exercise
    #for example for the repeat after me activity the app would generate its own word/sentence bank if progress was already made and the user was able to succeed past the first level of diffuculty
    #when the app first starts for a user the progress made will always be set to false

    #placeholder logic for now
    progress_made = False

    if not progress_made:
        return True
    else:
        return False
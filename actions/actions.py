# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import FollowupAction

from db_utils import establish_db_connection
from functions_cricket import *

class ActionRestart(Action):
    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            dispatcher.utter_message("Chat has been restarted.")
            return [Restarted()]
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return [AllSlotsReset()]

class ActionSelectFormat(Action):
    def name(self):
        return "action_format_selection"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            conn = establish_db_connection()

            buttons=[]
            
            buttons.append({"title": "ODI", "payload":'/odi_format{"format":"ODI"}'})
            buttons.append({"title": "T20", "payload":'/t20_format{"format":"T20"}'})
                
            dispatcher.utter_message(text="Please select the format..!",buttons=buttons)

        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []


class ActionSelectTournament(Action):
    def name(self):
        return "action_select_tournament_year"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            tournament_format=tracker.get_slot("format")
            conn = establish_db_connection()
            years=get_tournaments_years(tournament_format)

            if years:
                
                buttons=[]
                for row in years:
                    buttons.append({"title": row, "payload":'/select_tournament_year{"tournament_year":"' + str(row) + '" }'})
                    
                dispatcher.utter_message(text="please select "+tournament_format+" world cup held year to select the tournament..",buttons=buttons)

            else:
                dispatcher.utter_message(text="Sorry.. No matching data found ")

        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []


class CaptureCricketFormatAction(Action):
    def name(self) -> Text:
        return "action_select_format"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        tournament_format = next(tracker.get_latest_entity_values("format"), None)
        # tournament_format=tracker.get_slot("format")

        if tournament_format:
            format_value = tournament_format["value"].upper()
            if format_value in ["ODI", "T20"]:
                # Set the format slot
                tracker.slots["format"] = format_value
                dispatcher.utter_message(f"You selected {format_value} format. So ask what you need ? ")
            else:
                dispatcher.utter_message("Please choose a valid cricket format (ODI or T20).")
        else:
            # No format entity detected, trigger fallback action or utterance
            tracker.trigger_followup_action('action_format_fallback')

        return []
    
class ActionShowTournamentList(Action):
    def name(self):
        return "action_show_tournament_list"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            format=tracker.get_slot("format")
            conn = establish_db_connection()
            list_of_tournaments = get_tournaments(format)

            if list_of_tournaments:
                # Format the details list into a string
                dispatcher.utter_message(text="theese are the tournaments that i have access..")

                for row in list_of_tournaments:
                    dispatcher.utter_message(text=row)

            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")
                
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []

class ActionShowTeamList(Action):
    def name(self):
        return "action_show_team_list"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            conn = establish_db_connection()
            list_of_teams = get_teams()

            if list_of_teams:
                # Format the details list into a string

                dispatcher.utter_message(text="theese are the teams who plays international cricket ..")

                for row in list_of_teams:
                    dispatcher.utter_message(text=row)

            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []

class ActionShowPlayerOfTheSeies(Action):
    def name(self):
        return "action_show_player_of_the_series"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            tournament_year=tracker.get_slot("tournament_year")
            tournament_format=tracker.get_slot("format")
            conn = establish_db_connection()
            
            player_of_the_series=get_player_of_the_series(tournament_format, tournament_year)

            if player_of_the_series:
                dispatcher.utter_message(text="player of the series was "+player_of_the_series+"")
            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []


class ActionShowTournamentResult(Action):
    def name(self):
        return "action_show_tournament_result"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            tournament_year=tracker.get_slot("tournament_year")
            tournament_format=tracker.get_slot("format")
            conn = establish_db_connection()
            winning_team_of_the_series=get_winning_team_of_the_series(tournament_format, tournament_year)

            if winning_team_of_the_series:
                dispatcher.utter_message(text="winning team of the series was "+winning_team_of_the_series+"")
            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []

class ActionShowMostwicketstakerOfTheSeies(Action):
    def name(self):
        return "action_show_tournament_most_wicket_player"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            tournament_year=tracker.get_slot("tournament_year")
            tournament_format=tracker.get_slot("format")
            conn = establish_db_connection()
            most_wickets_taker_of_the_series=get_most_wickets_taker_of_the_series(tournament_format, tournament_year)

            if most_wickets_taker_of_the_series:
                dispatcher.utter_message(text="most wickets taken by "+most_wickets_taker_of_the_series+"")
            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []

class ActionShowMostRunsScorerOfTheSeies(Action):
    def name(self):
        return "action_show_tournament_most_run_player"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            tournament_year=tracker.get_slot("tournament_year")
            tournament_format=tracker.get_slot("format")
            conn = establish_db_connection()
            most_runs_scorer_of_the_series=get_most_runs_scorer_of_the_series(tournament_format, tournament_year)

            if most_runs_scorer_of_the_series:
                dispatcher.utter_message(text="most runs scored by "+most_runs_scorer_of_the_series+"")
            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []

class ActionShowhostOfTheSeies(Action):
    def name(self):
        return "action_show_host_of_the_series"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            tournament_year=tracker.get_slot("tournament_year")
            tournament_format=tracker.get_slot("format")
            conn = establish_db_connection()

            if not tournament_format:
                dispatcher.utter_message(text="format is not detected..")
                return [FollowupAction("action_format_selection")]
            
            if not tournament_year:
                dispatcher.utter_message(text="tournament year is not detected..")
                return [FollowupAction("action_select_tournament_year")]

            host_of_the_series=get_host_of_the_series(tournament_format, tournament_year)

            if host_of_the_series:
                dispatcher.utter_message(text="series was hosted in "+host_of_the_series+"")
            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")
            
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []

class ActionShowTournamentRunnerup(Action):
    def name(self):
        return "action_show_tournament_runnerup"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the list of available tournaments from your data source
        try:

            tournament_year=tracker.get_slot("tournament_year")
            tournament_format=tracker.get_slot("format")
            conn = establish_db_connection()
            runnerup_of_the_series=get_runnerup_of_the_series(tournament_format, tournament_year)

            if runnerup_of_the_series:
                dispatcher.utter_message(text="Runner up team of the series was "+runnerup_of_the_series+"")
            
            else:
                dispatcher.utter_message(text="Sorry.. No matching data found for your question")

        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []

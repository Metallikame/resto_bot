from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

class ActionVerifierCode(Action):
    def name(self) -> Text:
        return "action_verifier_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Récupère ce que l'utilisateur a donné comme code
        code_user = tracker.latest_message.get('text')

        # Vérifie si c'est le bon code
        if code_user and code_user.strip().upper() == "A123456":
            dispatcher.utter_message(response="utter_code_ok")
            return []
        else:
            dispatcher.utter_message(response="utter_code_faux")
            # Revenir au début (simuler retour au menu)
            return [UserUtteranceReverted()]

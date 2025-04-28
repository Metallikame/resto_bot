from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionVerifierCode(Action):

    def name(self) -> Text:
        return "action_verifier_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Ici tu récupères ce que l'utilisateur a dit
        code = tracker.latest_message.get('text')

        if code == "A123456":
            dispatcher.utter_message(text="Code correct ✅. Voici votre réservation : (détails fictifs).")
        else:
            dispatcher.utter_message(text="Code incorrect ❌. Merci de vérifier votre code.")

        return []

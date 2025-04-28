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
            dispatcher.utter_message(text="Code correct ✅. Voici les détails de votre réservation : \nCode de réservation : A123456\nNom : ROUZIOUX\nTel : 0102030405\nDate : 2023-04-18\nNombre de personnes : 4\n")
        else:
            dispatcher.utter_message(text="Code incorrect ❌. Merci de vérifier votre code.")

        return []

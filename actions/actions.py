from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideCourseInfo(Action):

    def name(self) -> Text:
        return "action_provide_course_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        curso = tracker.get_slot("curso")
        print(f"Curso recibido: {curso}")  # Esto te ayudará a depurar

        if curso == "Analisis de Datos":
            mensaje = "El curso de Análisis de Datos te enseñará a manejar y analizar datos utilizando herramientas como Excel, Python y SQL."
        elif curso == "Programacion":
            mensaje = "El curso de Programación cubre lenguajes como Python, Java y JavaScript, y te ayudará a desarrollar aplicaciones web y de software."
        elif curso == "Inteligencia Artificial":
            mensaje = "El curso de Inteligencia Artificial abarca conceptos de machine learning y deep learning, y cómo implementarlos en proyectos reales."
        else:
            mensaje = "No tengo información sobre ese curso. Si necesitas ayuda adicional, puedes contactar a nuestro asesor al número 555-1234."

        dispatcher.utter_message(text=mensaje)
        return []

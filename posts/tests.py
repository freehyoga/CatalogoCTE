# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from posts.models import Herramienta, Actividad, RecursoActividad, Tutorial, RecursoTutorial

# TEST MODELO HERRAMIENTA
class HerramientaModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba", fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, logo="logo", revisor1=1,revisor2=2,autor=0)

    def test_estado_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.estado_herramienta(), 1)

    def test_nombre_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.nombre_herramienta(), 'prueba')

    def test_url_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.url_herramienta(), 'www.google.com')

    def test_sistemaOperativo_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.sistemaOperativo_herramienta(), 'Windows')

    def test_plataforma_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.plataforma_herramienta(), 'Plataforma Prueba')

    def test_ficha_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.ficha_herramienta(), 'Ficha tecnica prueba')

    def test_licencia_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.licencia_herramienta(), 'gratis')

    def test_descripcion_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.descripcion_herramienta(), 'desc')

    def test_logo_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.logo_herramienta(), 'logo')


# # TEST PARA EL MODELO DE ACTIVIDAD
class ActividadModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba", fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, logo="logo", revisor1=1, revisor2=2, autor=0)
        herramienta=Herramienta.objects.get(nombre='prueba')
        Actividad.objects.create(herramienta=herramienta, nombre="actividadprueba", descripcion="descActividad", instrucciones="instruccionesPrueba", url="www.actividad.com", estado=1, revisor1=1, revisor2=2, autor=0)
#
    def test_descripcion_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.descripcion_actividad(), 'descActividad')

    def test_instrucciones_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.instrucciones_actividad(), 'instruccionesPrueba')

    def test_url_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.url_actividad(), 'www.actividad.com')

    def test_estado_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.estado_actividad(), 1)

    # def test_revisiones_actividad(self):
    #     tester = Actividad.objects.get(nombre='actividadprueba')
    #     self.assertEqual(tester.revisiones_actividad(), 0)

    def test_herramienta_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.herramienta_actividad(), 'prueba')


# TEST RECURSO ACTIVIDAD
class RecursoActividadModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba", fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, logo="logo", revisor1=1, revisor2=2, autor=0)
        herramienta = Herramienta.objects.get(nombre='prueba')
        Actividad.objects.create(herramienta=herramienta, nombre="actividadprueba", descripcion="descActividad", instrucciones="instruccionesPrueba", url="www.actividad.com", estado=1, revisor1=1, revisor2=2, autor=0)
        actividad=Actividad.objects.get(nombre='actividadprueba')
        RecursoActividad.objects.create(actividad=actividad, url="www.recurso.com", descripcion="descRecurso")

    def test_actividad_recurso_actividad(self):
        tester = RecursoActividad.objects.get(descripcion='descRecurso')
        self.assertEqual(tester.actividad_recurso_actividad(), 'actividadprueba')

    def test_url_recurso_actividad(self):
        tester = RecursoActividad.objects.get(descripcion='descRecurso')
        self.assertEqual(tester.url_recurso_actividad(), 'www.recurso.com')

    def test_descripcion_recurso_actividad(self):
        tester = RecursoActividad.objects.get(descripcion='descRecurso')
        self.assertEqual(tester.descripcion_recurso_actividad(), 'descRecurso')

class TutorialModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba",fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, revisor1=1, revisor2=2, autor=0, logo="logo")
        herramienta = Herramienta.objects.get(nombre='prueba')
        Tutorial.objects.create(herramienta=herramienta, nombre="tutorialPrueba", funcionalidad="funcionalidadTutorial", estado=1, revisor1=1, revisor2=2, autor=0)

    def test_herramienta_tutorial(self):
        tester = Tutorial.objects.get(nombre='tutorialPrueba')
        self.assertEqual(tester.herramienta_tutorial(), 'prueba')

    def test_nombre_tutorial(self):
        tester = Tutorial.objects.get(nombre='tutorialPrueba')
        self.assertEqual(tester.nombre_tutorial(), 'tutorialPrueba')

    def test_funcionalidad_tutorial(self):
        tester = Tutorial.objects.get(nombre='tutorialPrueba')
        self.assertEqual(tester.funcionalidad_tutorial(), 'funcionalidadTutorial')

    def test_estado_tutorial(self):
        tester = Tutorial.objects.get(nombre='tutorialPrueba')
        self.assertEqual(tester.estado_tutorial(), 1)

    # def test_revisiones_tutorial(self):
    #     tester = Tutorial.objects.get(nombre='tutorialPrueba')
    #     self.assertEqual(tester.revisiones_tutorial(), 0)

class RecursoTutorialModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba",fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, revisor1=1, revisor2=2, autor=0, logo="logo")
        herramienta = Herramienta.objects.get(nombre='prueba')
        Tutorial.objects.create(herramienta=herramienta, nombre="tutorialPrueba", funcionalidad="funcionalidadTutorial", estado=1, revisor1=1, revisor2=2, autor=0)
        tutorial=Tutorial.objects.get(nombre='tutorialPrueba')
        RecursoTutorial.objects.create(tutorial=tutorial, url='www.recTutorial.com', descripcion='descRecuTuto')

    def test_tutorial_recurso_tutorial(self):
        tester = RecursoTutorial.objects.get(descripcion='descRecuTuto')
        self.assertEqual(tester.tutorial_recurso_tutorial(), 'tutorialPrueba')

    def test_url_recurso_tutorial(self):
        tester = RecursoTutorial.objects.get(descripcion='descRecuTuto')
        self.assertEqual(tester.url_recurso_tutorial(), 'www.recTutorial.com')

    def test_descripcion_recurso_tutorial(self):
        tester = RecursoTutorial.objects.get(descripcion='descRecuTuto')
        self.assertEqual(tester.descripcion_recurso_tutorial(), 'descRecuTuto')
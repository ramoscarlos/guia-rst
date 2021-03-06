¿Qué se puede hacer?
====================



Ya vimos que reST es un lenguaje de escritura eficiente y sirve porque se puede convertir a otros formatos... pero ¿cuáles son esos formatos? ¿qué beneficios tiene de verdad el escribir en reST para luego traducir?

En este capítulo veremos los formatos a los que podemos convertir reST, dividido en dos secciones principales. Primero, lo que puedes hacer desde el editor en línea y, segundo, lo que puedes hacer desde Sphinx. Esto último se incluye para que, si reST es de tu agrado, conozcas el alcance de lo que puedes lograr.



Con el editor en línea
----------------------



La compilación con el editor en línea solamente permite dos formatos de salida:

+ HTML (página web)
+ PDF

Esto es suficiente para los fines de esta obra ya que con eso podrás probar el potencial de reST y su sintaxis, para que después decidas si quieres continuar tu jornada con Sphinx.

Además, tiene utilidad: puedes exportar a PDF para compartir tus notas con otras personas con facilidad.



Con Sphinx
----------



Ahora, si decides que reST es para ti y deseas ampliar tus posibilidades, ¿qué te permitirá hacer Sphinx?



Sitios web
^^^^^^^^^^



Podrás crear sitios web completos, con múltiples páginas, porque Sphinx cuenta con un generador HTML de sitios estáticos. Sí, está orientado para proyectos de documentación, pero eso no impide que puedas crear un blog a partir de él (especialmente si no requieres comentarios en tu sitio).



Documentos
^^^^^^^^^^



Además de generar el sitio, puedes convertir a PDF (aunque esto ya lo esperabas gracias al editor en línea). Esto lo hace a través de LaTeX. Si estás familiarizado con ese lenguaje, también puedes personalizar el formato de salida de tu PDF.

Imagina: poder crear tanto el sitio web de tu contenido, como todo un PDF que puede ser un libro. Todo con el mismo código fuente.

Claro, no estoy diciendo que harás un documento tan espectacular como te lo permiten todas las opciones de Microsoft Word, o incluso otros programas especializados para la edición de PDFs, pero este libro fue creado con Sphinx, todo escrito en reStructuredText. ¿No crees que es genial?



Libros electrónicos
^^^^^^^^^^^^^^^^^^^



¿No acabamos de mencionar PDF en el apartado anterior? Sí, pero no me refiero a eso. Me refiero al formato electrónico de libros EPUB. Después de todo, el formato EPUB es un subconjunto de HTML, ¿por qué no iba a ser posible?

Si quieres escribir un libro de manera independiente, puedes usar Sphinx y reST para escribir una vez y exportar tanto a PDF como a EPUB, además de poder tener tu libro en línea en formato HTML. Tres formatos por el precio de uno. ¿Por qué no?



Notas
^^^^^



El formato reST también es bastante útil a la hora de escribir notas rápidas. Colocas un título, e inicias una lista de viñetas rápidamente. Así puedes iniciar la lista de lo que debes comprar en el súpermercado, o los pendientes del día.

¿Quizá notas del trabajo? Separas cada parte con un subtítulo, y listo. Mucho mejor que tener notas en texto plano.

Lo malo: para tomar notas en reST no hay plataformas en línea o apps para tu teléfono celular. Solo puedes lograrlo en un editor en línea o en tu computadora de manera local con un programa como Atom_ o `Sublime Text`_, usando el resaltado de sintaxis para archivos *\*.rst*.



Documentación
^^^^^^^^^^^^^



En documentación es donde reStructuredText, en conjunto con Sphinx, brilla. Sitios como `Read The Docs`_ y `Write The Docs`_ son potenciados por Sphinx.

Si tienes un proyecto de código libre y deseas publicar documentación puedes enlazar tu repositorio de GitHub a un proyecto de `Read The Docs`_ y *voilà*, ¡documentación disponible!



Resumen
-------



En este capítulo vimos que reST puede servirte para hacer notas en un editor en línea, que convierte el código reST a HTML visualmente agradable. Además, este editor permite exportar el contenido a un PDF, ¡una forma conveniente de tomar notas!

Además, en conjunto con Sphinx, reST puede crear sitios web de documentación completos, además de libros completos en formato PDF o EPUB. ¿Qué más le puedes pedir a reStructuredText?



.. _Atom: https://atom.io/
.. _Sublime Text: https://www.sublimetext.com/
.. _Read The Docs: https://readthedocs.org/
.. _Write The Docs: https://www.writethedocs.org/
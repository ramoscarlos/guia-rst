Directivas
==========



Las directivas son instrucciones especiales de reStructuredText que comienzan por ``..`` y un espacio, seguido del nombre de la directiva, que terminan con ``::``, y cualquier argumento que se reciba. Es decir:

.. code-block:: rst

    .. directiva:: argumentos

Además, pueden tener opciones, mismas que se delimitan por ``:`` al inicio y al final, además del contenido. Por lo tanto, la "forma completa" de una directiva es:

.. code-block:: rst

    .. directiva:: argumentos
        :opcion1:
        :opcion2:

            contenido

Antes de empezar este capítulo es necesario informarte que no podrás probar varias de las directivas aquí mencionadas. Esto es porque requieren de archivos locales ubicados en la misma carpeta que tu archivo de reST. Y, sí, los editores en línea no cuentan con esa facilidad.

Una vez hecha la advertencia, la primer directiva que veremos es ``image``.



Imágenes
--------



La directiva ``image`` se utiliza con un argumento obligatorio: el directorio o dirección donde se ubica la imagen. Por ejemplo, aquí debajo incluyo mi logo personal, alojado en mi dominio:

.. code-block:: rst

    .. image:: http://ramoscarlos.com/logo.png

Con eso basta para que reST pueda ir por la imagen y colocarla en mi documento:

.. image:: http://ramoscarlos.com/logo.png

No obstante, dependiendo del ancho de tu pantalla, el contenido puede aparecer desbordado. Esto pasa porque reST no le hace ningún tipo de procesamiento o escalado a la imagen. Aquí es donde entran las opciones, para poder darle formato a la imagen:

:height: es el alto de la imagen, utilizado para reservar espacio vertical para la imagen. Cuando se utiliza en conjunto con la opción de ``scale``, ambos se aplican (por ejemplo, escala al 40% de 100px da 40px).
:width: es el ancho de la imagen, y puede ser en términos absolutos o en porcentaje. De manera análoga a la altura, se combina con la opción de escala.
:scale: es un factor de escalamiento, en porcentaje, que se aplicará a la imagen (el símbolo de porcentaje puede omitirse). El valor predeterminado es 100% (sin escalamiento).
:align: la alineación de la imagen, puede tener los siguientes valores: ``top``, ``middle``, ``bottom``, ``left``, ``center``, o ``right``. Los primero tres valores hacen referencia a la alineación vertical, mientras que los últimos tres hacen referencia a su posición horizontal.
:alt: es un texto alternativo a utilizar en caso de que no se pueda desplegar la imagen. También es texto que se lee por aplicaciones de asistencia visual.
:target: sirve para hacer que la imagen sea un enlace hacia la URL o referencia de esta opción.

Después de haber visto las opciones, lo primero que probaremos es el uso de ``alt`` sobre una imagen inexistente. Por ejemplo:

.. code-block:: rst

    .. image:: http://yo-no-existo.com/ni-existire.gif
        :alt: Referencia a imagen inexistente.

Al colocar el código de la imagen, lo único que se desplegará es el texto:

.. image:: http://yo-no-existo.com/ni-existire.gif
    :alt: Referencia a imagen inexistente.

Ahora bien, a resolver el problema de la imagen que desborda los márgenes, ya sea de la página web o de la hoja de un libro físico. Para ello usamos la opción ``width``, con un valor del 100% del ancho, y no más. Además, aprovechamos para colocar un texto alternativo:

.. code-block:: rst

    .. image:: http://ramoscarlos.com/logo.png
        :width: 100%
        :alt: Logo de ramoscarlos.com

.. image:: http://ramoscarlos.com/logo.png
    :width: 100%
    :alt: Logo de ramoscarlos.com



Imágenes locales
^^^^^^^^^^^^^^^^



La directiva ``image`` no sirve únicamente para colocar imágenes provenientes de Internet. Por supuesto, esto no es algo que se pueda probar en el editor en línea. No obstante, haciendo uso de Sphinx podrías incluir cualquier imagen dentro de tu disco duro, con la trayectoria completa (empezando desde ``C:/``, si fuera Windows) o, lo más común, desde un directorio relativo a tu proyecto.

En caso de trabajar localmente, lo más común es guardar las imágenes en el subdirectorio ``img`` (o algo por el estilo) relativo a tu archivo reST. Y ya, automáticamente reStructuredText sabe en qué lugar ir a buscar el archivo de tu imagen. Una muestra de tal sintaxis sería:

.. code-block:: rst

    .. image:: img/nombre-de-imagen.png



Figuras
-------



Una figura es una imagen con una leyenda debajo. Su sintaxis es similar a la directiva ``image``, y acepta sus opciones, solo que agrega el contenido de la directiva, que corresponde a la leyenda que se colocará debajo de la imagen:

.. code-block:: rst

    .. figure:: img/nombre-de-imagen.png

        Leyenda de la figura.

Podemos tomar uno de los ejemplos anteriores, y duplicar el texto de la opción ``alt`` para usarla como el contenido de la directiva (leyenda):

.. code-block:: rst

    .. figure:: http://ramoscarlos.com/logo.png
        :width: 60%
        :alt: Logo de ramoscarlos.com

        Logo de ramoscarlos.com (con leyenda)

Y listo, tenemos una imagen con leyenda:

.. figure:: http://ramoscarlos.com/logo.png
    :width: 60%
    :alt: Logo de ramoscarlos.com

    Logo de ramoscarlos.com (con leyenda)



Código fuente (embebido)
------------------------



No solamente podemos incluir código como :ref:`texto preformateado <texto-preformateado>`, sino que podemos colocar código fuente formalmente, con resaltado de sintaxis, gracias a la directiva ``code``, que recibe como argumento el lenguaje en que el código está escrito.

Dado que el código se resalta con la librería Pygments_, los lenguajes disponibles son los mismos de esta librería... que son bastantes.

Pongamos por ejemplo un fragmento de código C:

.. code:: c

    int main() {
        return 0;
    }

Ese código se muestra con la sintaxis adecuada gracias a su argumento:

.. code-block:: rst

    .. code:: c

        int main() {
            return 0;
        }

Incluso podemos resaltar reStructuredText:

.. code:: rst

    Esto está en *italicas* y esto en **negritas**.

Donde el código detrás es:

.. code-block:: rst

    .. code:: rst

        Esto está en *italicas* y esto en **negritas**.

.. note::

    Es posible que los editores en línea no carguen las sintaxis debido a que esto implica más procesamiento y es un poco más difícil de lograr. No obstante, a través del uso de Sphinx puedes ver este comportamiento, aunque eso está fuera del alcance de este libro.



Opción ``number-lines``
^^^^^^^^^^^^^^^^^^^^^^^


La directiva ``code`` tiene la opción ``number-lines``, la cual nos permite colocar números de línea. Volviendo al ejemplo de C, podemos agregar los números de línea con:

.. code-block:: rst

    .. code:: c
        :number-lines:

        int main() {
            return 0;
        }

Lo que ahora genera un código como:

.. code:: c
    :number-lines:

    int main() {
        return 0;
    }

También podemos cambiar el número inicial agregando el argumento después de los dos puntos de la opción:

.. code-block:: rst

    .. code:: c
        :number-lines: 50

        int main() {
            return 0;
        }

Lo que ahora despliega la primera línea como la 50:

.. code:: c
    :number-lines: 50

    int main() {
        return 0;
    }

Es importante colocar al menos un espacio entre el número inicial y ``number-lines``, de lo contrario tendrás una advertencia sobre exceder el número de argumentos y tu código no se verá:

.. code-block:: none

    WARNING: Error in "code" directive:
    maximum 1 argument(s) allowed, 2 supplied.

    .. code:: c
            :number-lines:50

            int main() {
                    return 0;
            }



Código fuente (archivo externo)
-------------------------------

Si prefieres insertar código de un archivo fuente en lugar de copiar y pegar fragmentos, entonces la directiva ``include`` es lo que buscas. Sí, lo sé, esto no lo puedes probar en línea.

Su sintaxis es similar a la directiva ``image``, en el sentido de que su argumento requerido es la trayectoria del archivo relativo al archivo fuente (aunque aquí no se permiten recursos en línea).

Recomiendo guardar el código fuente en un subdirectorio. En este libro se hace referencia al directorio ``src``. Para esta demostración tomé el código fuente de un ejemplo de alcance de la `documentación oficial de Python <https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example>`_ y lo guardé como ``demo.py`` en la carpeta antes mencionada.

Para incluir el archivo simplemente usamos la directiva ``include`` con la trayectoria relativa al archivo:

.. code-block:: rst

    .. include:: src/demo.py

Lo que nos incluye el código:

.. include:: src/demo.py

No obstante, eso imprime el código sin resaltado de sintaxis, comiéndose algunos saltos de línea... debido a que interpreta el texto siguiendo las reglas de reStructuredText (claro, no le hemos dicho lo contrario).



Opción ``code``
^^^^^^^^^^^^^^^

Los errores de visualización del ejemplo anterior se pueden arreglar con la opción ``code``, que toma como argumento el lenguaje con el cual resaltar el archivo incluído. Recordemos que el resaltado se realiza gracias a Pygments, así que cualquier lenguaje que funciona para ``code``, funciona con la opción ``code`` del ``include``. Reescribiendo:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python

Ya podemos ver nuestro archivo como código Python:

.. include:: src/demo.py
    :code: python



Opción ``number-lines``
^^^^^^^^^^^^^^^^^^^^^^^

También acepta el número de línea inicial a mostrarse, similar al entorno ``code``, con la opción ``number-lines``:

.. include:: src/demo.py
    :code: python
    :number-lines:

No obstante, aquí se aprecia una diferencia contra ``code``: el resaltado de sintaxis se pierde, y la selección del texto incluye los números de línea.

La lección: usar ``code`` si se requieren números de línea.



Opciones ``start-line`` y ``end-line``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

También podemos incluir un fragmento, especificando de qué a qué línea. Por ejemplo, si solo queremos ver la función ``do_global``, que se encuentra de las líneas 9 a 11, usamos la opción ``start-line`` con un valor de 8, porque el conteo empieza en 0, y ``end-line`` con 12, dado que el número de línea que recibe como argumento no se imprime:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :start-line: 8
        :end-line: 12

Lo que nos muestra el código de la función como deseamos:

.. include:: src/demo.py
    :code: python
    :start-line: 8
    :end-line: 12

Lamentablemente, el resaltado de sintaxis se pierde al usar estos parámetros debido a que no sabe qué hacer con los diferentes niveles de indentación. Es decir, este método no es tan confiable para mostrar ciertas líneas y a la vez colorearlas. Ugh.



Opciones ``start-after`` y ``end-after``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pero si queremos siempre imprimir la función ``do_global``, independientemente del número de línea, ¿cómo le hacemos?

Existe otra opción que incluye código en base a cadenas de texto, llamada ``start-after``, así podemos usar ``:start-after: "non-local spam"`` para empezar en nuestra línea de función:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :start-after: "nonlocal spam"

Aunque también perdemos el coloreado, aunque el código es correcto:

.. include:: src/demo.py
    :code: python
    :start-after: "nonlocal spam"

Podemos aplicar la misma lógica para definir el contenido hasta la línea que ya no queremos imprimir, en este caso ``spam = "test spam"``:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :start-after: "nonlocal spam"
        :end-before: spam = "test spam"

Y el resultado es similar a haber utilizado los números de línea:

.. include:: src/demo.py
    :code: python
    :start-after: "nonlocal spam"
    :end-before: spam = "test spam"



Opción ``tab-width``
--------------------

La opción ``tab-width`` nos permite establecer el ancho de las tabulaciones, que de manera predeterminada es 8 espacios.

Por ejemplo, para establecer la tabulación a dos espacios usaríamos:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :tab-width: 2

.. include:: src/demo.py
    :code: python
    :tab-width: 2

Si parece no funcionar, hay que revisar si nuestro archivo contiene tabulaciones...

En este caso, esos puntos nos indican que el archivo usa espacios, no tabulaciones. Podemos cambiar cuatro espacios por una tabulación, para observar el efecto de este parámetro...

.. include:: src/demo.py
    :code: python
    :tab-width: 2

En caso de no especificar este parámetro, el valor predeterminado es 8 espacios:

.. include:: src/demo.py
    :code: python

Aunque, claro, mi recomendación es no usar este parámetro, porque es mejor usar cuatro espacios siempre.



HTML o LaTeX con ``raw``
------------------------



Si sientes la imperiosa necesidad de colocar HTML en tu documento de reST, no es así de simple. Probemos con una regla horizontal en HTML:

<hr>

Sí, no funciona. Para insertar HTML directo se puede utilizar la directiva ``raw``, con el argumento del lenguaje que se utilizará para interpretar el contenido, que en este caso es ``html``:

.. code-block:: rst

    .. raw:: html

        <hr>

Y ahora sí, eso da como resultado la regla horizontal:

.. raw:: html

    <hr>

... por supuesto, para los lectores del PDF no hay nada entre el párrafo anterior y este. Eso es porque el PDF compila LaTeX, no HTML (razón para no usar HTML directo). Pero si queremos una línea horizontal en el PDF podemos usar ``\rule`` en un entorno LaTeX:

.. code-block:: rst

    .. raw:: latex

        \noindent{\rule{\linewidth}{0.4pt}}

Y eso nos da una línea horizontal en el PDF, pero no en la página web de HTML:

.. raw:: latex

    \noindent{\rule{\linewidth}{0.4pt}}

De esta manera podemos incluir tanto HTML y LaTeX como nuestro corazón desee. Por supuesto, si se desea compilar tanto en HTML como en LaTeX, habrá que proveer ambas opciones, en cada lenguaje. Por ejemplo, podríamos poner las dos instrucciones seguidas:

.. code-block:: rst

    .. raw:: html

        <hr>

    .. raw:: latex

        \noindent{\rule{\linewidth}{0.4pt}}

De esta manera, tanto en HTML como en LaTeX tenmos nuestra regla debajo:

.. raw:: html

    <hr>

.. raw:: latex

    \noindent{\rule{\linewidth}{0.4pt}}

También puedes incluir todo un archivo, mediante la opción ``:file: subdirectorio/archivo.html``, aunque sigue sin ser recomendado su uso.



Amonestaciones
--------------



Las amonestaciones son notas o temas especiales que aparecen marcados a lo largo del texto. En el caso de HTML, puedes imaginar cajas de colores: roja para errores, amarilla para advertencias, azules para información. En el caso de libros, puedes pensar en pequeños textos como en las series "Para Dummies", que incluyen consejos, advertencias, o simples notas a considerar.

La amonestación no es una sola directiva, si no que son un conjunto, que son las siguientes: ``attention``, ``caution``, ``danger``, ``error``, ``hint``, ``important``, ``note``, ``tip``, y ``warning``.

Dependiendo de tu tema en HTML, cada una de estas amonestaciones tiene un estilo diferente, y se mandan llamar de la siguiente forma:

.. code-block:: rst

    .. nombre-del-tipo-de-amonestación::

        Contenido de la amonestación.

Por ejemplo, para crear un cuadro de atención, usamos su nombre como directiva:

.. code-block:: rst

    .. attention::

        Contenido de la amonestación.

Y ahora veremos el estilo que cada una de estas diferentes amonestaciones puede tener (que, de nuevo, varían según tu tema):

.. attention::

    Contenido de la amonestación ``attention``.

.. caution::

    Contenido de la amonestación ``caution``.

.. danger::

    Contenido de la amonestación ``danger``.

.. error::

    Contenido de la amonestación ``error``.

.. hint::

    Contenido de la amonestación ``hint``.

.. important::

    Contenido de la amonestación ``important``.

.. note::

    Contenido de la amonestación ``note``.

.. tip::

    Contenido de la amonestación ``tip``.

.. warning::

    Contenido de la amonestación ``warning``.

Ahora bien, cada una de las amonestaciones anteriores colocan el título y un estilo predeterminado. No obstante, nos queda una última amonestación, la cual es genérica. ¿Qué quiere decir? Que no contiene un título, por lo que recibe el título de la amonestación como parámetro requerido:

.. code-block:: rst

    .. admonition:: Título de la amonestación.

        Contenido de la amonestación ``admonition``.

Lo que da como resultado:

.. admonition:: Título de la amonestación.

    Contenido de la amonestación ``admonition``.



Matemáticas
-----------



Sí, reStructuredText también sirve para lidiar con complejas ecuaciones matemáticas... bueno, más o menos. Para ello hace uso de LaTeX. Así que, si conoces LaTeX, estás salvado y solo tienes que saber que puedes incluir ecuaciones con la directiva ``math``:

.. code-block:: rst

    .. math::

        \frac{1}{2} + \frac{1}{4} + \ldots = \sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n = 1

Lo que, por supuestos, se resuelve a:

.. math::

    \frac{1}{2} + \frac{1}{4} + \ldots = \sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n = 1

Si desconoces LaTeX, `escribí un libro que podría ayudarte con ello`_.



Extensibilidad
--------------



En los primeros capítulos se hablo de la extensibilidad de reST pero no ahondamos mucho en ese tema. Como vimos al inicio de este capítulo, una directiva es algún nombre entre ``..`` y ``::``. En teoría, podemos hacer una directiva para mostrar una lista de asistencia de tres semanas:

.. code-block:: rst

    .. lista-de-asistencia::
        :grado: 5
        :grupo: G

        Juanito Pérez
        Marianita López

Y, de alguna manera mística, que eso se convierta en una tabla con fechas y todo, ¿por qué no? Bueno... porque esto sí implica saber programar en Python y ser capaz de poder seguir la gúia de `Creating reStructuredText Directives`_ (sí, en inglés).

Entonces, mientras que Markdown lograba más funcionalidad debido a sus sabores y adiciones por terceros, reST cuenta con un sistema para ser extendido. Incluso hay formas de que tus contribuciones se añadan a un repositorio oficial, y que lo instale quien necesita.

Claro, para eso ya hablamos más de Sphinx, y la mayoría de las extensiones están en inglés, pero hay bastantes disponibles. Puedes encontrar lo que la comunidad ha cooperado en `sphinx-contrib`_.



Resumen
-------



En este capítulo vimos las directivas de reST, que resultan no ser solo instrucciones más potentes sino que son la base del mecanismo de extensibilidad del lenguaje.

Aunque en esta obra nos limitamos a las directivas definidas en la especificación de reST, nada nos detiene de ir a husmear qué es lo que otras personas han considerado pertinente agregar a este lenguaje.



.. #######################################################################
.. ### Enlaces externos ##################################################
.. #######################################################################

.. _Pygments: https://pygments.org/languages/
.. _escribí un libro que podría ayudarte con ello: https://leanpub.com/tesis-en-latex/
.. _Creating reStructuredText Directives: https://docutils.sourceforge.io/docs/howto/rst-directives.html
.. _sphinx-contrib: https://github.com/sphinx-contrib/
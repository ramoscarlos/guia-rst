Sintaxis básica
===============



En este capítulo se cubre lo necesario para empezar a utilizar reST en tu día a día, y tiene como objetivo servir como referencia en caso de que olvides cómo hacer algo en particular.



Párrafos y líneas en blanco
---------------------------



Para escribir párrafos solamente tienes que escribir, así como si nada, sin ningún indicador especial. No obstante, antes de crear dos párrafos es necesario hablar de las líneas en blanco... porque el siguiente texto
equivale solamente a
una línea de texto
(o un párrafo):

.. code-block:: rst

    porque el siguiente texto
    equivale solamente a
    una línea de texto
    (o un párrafo)

Es decir, un salto de línea se reduce a solamente un espacio dentro de reST, por lo que para         crear           un nuevo párrafo se requiere una línea vacía entre ambos:

.. code-block:: rst

    Este es un párrafo.

    Este es otro párrafo gracias a la línea vacía.

Esto nos lleva a hablar de ¿qué pasa si hay dos líneas en blanco? ¿o tres? ¿o cincuenta? Lo que pasa es lo mismo: un cambio de párrafo, no hay más.

¿Y el espacio en blanco entre cada palabra? Estos se colapsan a solamente uno. Es decir, escribir lo siguiente:

.. code-block:: rst

    Este       enunciado     con       mucho        espacio.

.. raw:: latex

    \newpage

En realidad se muestra simplemente así:

.. code-block:: rst

    Este enunciado con mucho espacio.

En resumen, al escribir en reST hay que tomar en cuenta tres cosas:

1. Para cambiar de párrafo se requiere al menos una línea en blanco entre ambos párrafos.
2. Dos o más líneas en blanco tienen el mismo efecto: solo un cambio de párrafo.
3. Cualquier cantidad de espacios en blanco se reduce solamente a uno.



¿Pero qué pasa si quiero más líneas en blanco?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Si de verdad necesitas más líneas en blanco entre dos párrafos puedes utilizar una barra vertical como único contenido de una línea. Con eso lograrás más separación entre un párrafo y otro. Por ejemplo,

|
|

esta separación se logró con el siguiente código en reST:

.. code-block:: rst

    Por ejemplo,

    |
    |

    esta separación se logró con el siguiente código en reST.



Citas e indentación
-------------------



Ahora bien, también podemos crear citas, o frases, indentando un poco el texto. Es decir, si quisiera citar a Martin Luther King solamente debería escribir la cita con una ligera indentación. Esto es, con al menos un espacio antes de empezar a escribir:

    Las tensiones no son entre las razas, sino entre las fuerzas de la justicia y la injusticia

Para que lo anterior se viera como una frase solamente fue necesario escribirlo con el siguiente formato:

.. code-block:: rst

    párrafo

        frase

    párrafo

En otras palabras, un párrafo siempre está pegado al margen izquierdo y una frase siempre está indentada. No obstante, ¿qué se considera indentación? La indentación es cualquier número de espacios en blanco mayor a cero. Puede ser un espacio, cuatro, cincuenta, y el efecto sería el mismo.

Si a la frase le queremos agregar el autor, podemos continuar escribiendo en la frase mientras no abandonemos la indentación:

    Las tensiones no son entre las razas, sino entre las fuerzas de la justicia y la injusticia

    Martin Luther King

¿Y si queremos colocar una frase dentro de otra frase? Simplemente creamos un nuevo nivel de indentación:

    Las tensiones no son entre las razas, sino entre las fuerzas de la justicia y la injusticia

        Martin Luther King

De tal manera que podemos resumir lo anterior con el siguiente ejemplo:

.. code-block:: rst

    párrafo antes de la frase.

        frase 1.

            frase 2, por indentación diferente.

        frase 1, por indentación inicial.

    párrafo después de la frase, sin indentación.

Con este ejemplo de las citas vemos otras dos características importantes de reST:

1. La indentación importa y tiene un significado.
2. La indentación puede contener cualquier número de espacios.



Formato básico
--------------



Al referirme al formato básico me refiero a itálicas, negritas, y fuente de ancho fijo para código. En los tres casos, el símbolo en cuestión se utiliza tanto al inicio como al final de la cadena que se quiere modificar, como se muestra en la siguiente tabla:



========== ======= =======================
Estilo     Símbolo Ejemplo
---------- ------- -----------------------
Itálicas   \*      *\*Texto en itálicas\**
Negritas   \*\*    **\*\*Texto en negritas\*\***
Ancho fijo \`\`    ````Texto de ancho fijo````
========== ======= =======================

Cabe destacar que no es posible mezclar dos de estos formatos juntos. Es decir, si quieres itálicas con negritas, encerrar el texto entre tres símbolos de estrella no servirá de mucho: ***he aquí la muestra*** (lo anterior fue texto entre tres estrellas, dos se usaron para las negritas, y una se imprimió).

De igual manera, el ancho fijo y negritas da resultados no deseados. Por ejemplo, **``este texto empieza con negritas, dentro ancho fijo``**, y este ``**es ancho fijo con negritas dentro**``. Dados lo ejemplos anteriores podemos concluir que en reST solo podemos marcar el texto con un formato y, en caso de que más de uno se utilice, se usará el más externo (o el primero colocado).



Encabezados (títulos)
---------------------



En sí, un encabezado es una línea de texto que está seguida de una línea de símbolos iguales de al menos la misma longitud que el título. Por ejemplo, el título de este capítulo se escribió como:

.. code-block:: rst

    Sintaxis básica
    ===============

Pero bien pudo haber sido con guiones cortos en lugar de símbolos de igual, con el mismo resultado:

.. code-block:: rst

    Sintaxis básica
    ---------------

¿Y qué símbolos pueden ser utilizados para denotar un título? Oficialmente, la descripción solamente dice "cualquier carácter ASCII de 7 bits no alfanumérico". Es decir, los siguientes símbolos aplican: ``= - ` : ' " ~ ^ _ * + # < >``.

Por lo que bien podríamos poner el título del capítulo como:

.. code-block:: rst

    Sintaxis básica
    >>>>>>>>>>>>>>>

No obstante, y aunque no es parte propiamente parte de reStructuredText si no de Sphinx, se sigue el siguiente estándar:

- ``=``, para secciones.
- ``-``, para subsecciones.
- ``^``, para subsubsecciones.
- ``"``, para párrafos.

También puedes colocar una línea antes del título (además de la de que va después) para denotar un título aún más "superior". Este sería un ejemplo:

.. code-block:: rst

    ===============
    Sintaxis básica
    ===============

Según Sphinx, estas otras dos opciones están disponibles para libros:

- ``=``, con línea arriba y abajo, para partes.
- ``*``, con línea arriba y abajo, para capítulos.

Dado que eso aplica más bien en libros, para las notas del día a día, o simples manuales, basta con reconocer que varios símbolos pueden ser utilizados para crear secciones, y que dependen del orden de aparición.

Es decir, considérense los siguientes dos ejemplos, donde el título y el subtítulo no cambian, aunque sus símbolos de línea sí:

.. code-block:: rst

    Este es un título
    =================

    Este es un subtítulo
    --------------------

Lo anterior es equivalente a lo siguiente:

.. code-block:: rst

    Este es un título
    -----------------

    Este es un subtítulo
    ====================

.. raw:: latex

    \newpage

Aunque lo puedas hacer, y sea técnicamente correcto, es mejor limitarse a un patrón mental de referencia que sea consistente. Es decir, adoptar algo como: ``=`` es para títulos, ``-`` es para subtítulos, y ``^`` es para subsubtítulos, y otros más si llegas a necesitar aún más símbolos.



Vale, vale, ¿pero qué pasa si la regla es de menor longitud?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Lo que ocurrirá si creas un título con su regla inferior de menor longitud es que tendrás una advertencia:

.. code-block:: none

    WARNING: Title underline too short.

Y nada más. El título (o subtítulo, o el nivel que sea) se creará de manera correcta. No obstante, recomiendo tener como objetivo el no generar advertencias de compilación en tu documento. Ya sabes, por eso de la `teoría de las ventanas rotas`_.



Comentarios
-----------



Para escribir comentarios se inicia una línea solo con dos puntos y un espacio, y cualquier cosa después de ellas no se mostrará en el documento. Por ejemplo:

.. Esta línea es un comentario y no aparece en el texto transformado.

.. code-block:: rst

    .. Esta línea es un comentario y no aparece en el texto transformado.

Para escribir un comentario de múltiples líneas solamente continúa escribiendo texto con una indentación de al menos un espacio. La convención aquí es utilizar tres espacios, para que las líneas del comentario aparezcan alineadas:

.. Esta línea es un comentario.
   De hecho esta también.

   Y todas hasta que se deja la indentación.

.. code-block:: rst

    .. Esta línea es un comentario.
       De hecho esta también.

       Y todas hasta que se deja la indentación.

Como se ve en el ejemplo, el comentario no se pierde con líneas vacías, sino que se termina cuando dejas la indentación y comienzas un párrafo u otra instrucción.



Listas
------



Existen tres listas diferentes en reStructuredText: sin orden, con orden, o diccionarios. En los tres casos, se pueden anidar, mientras que la cantidad de espacios sean los mismos de un nivel a otro.



Listas sin orden
^^^^^^^^^^^^^^^^



Las listas sin orden, o con viñetas, se pueden crear con el símbolo de estrella (``*``), el signo de más (``+``), o el signo de menos (``-``). Por ejemplo, aquí una lista:

- Primer elemento.
- Segundo elemento.
- Tercer elemento.

El código para esa lista fue:

.. code-block:: rst

    - Primer elemento.
    - Segundo elemento.
    - Tercer elemento.

Aunque bien pudo haber sido el siguiente:

.. code-block:: rst

    + Primer elemento.
    + Segundo elemento.
    + Tercer elemento.

Es decir, no importa cuál de los tres símbolos utilices, el resultado será la misma viñeta. No obstante, procura no mezclar dos o más símbolos dentro del mismo nivel porque eso producirá la siguiente advertencia:

.. code-block:: none

    WARNING: Bullet list ends without a blank line; unexpected unindent.

¿Qué pasa aquí? El convertidor de reStructuredText sse confundió un poco. Espera que una lista tenga solo un símbolo, y si tiene dos cree que es por una de las siguientes dos razones:

1. Espera que el segundo símbolo utilizado corresponda a otra lista independiente, pero de ser así, falta una línea que divida ambas listas (cosa que no pasó).
2. Quieres hacer dos niveles, una lista dentro de otra, aunque para eso hace falta un poco de indentación (cosa que tampoco pasó).

En su resignación, te crea una lista de manera adecuada, pero mandando la advertencia para que resuelvas el problema, en caso de que una de las suposiciones anteriores sea correcta.



Listas anidadas
^^^^^^^^^^^^^^^



Ahora bien, si queremos una lista dentro de otra dentro de otra dentro de otra necesitamos seguir dos reglas de reST, y una agregada por LaTeX:

1. Cada lista anidada debe estar separada por una línea vacía respecto a su lista madre, y los elementos sucesores de la lista madre.
#. La indentación aquí no es arbitraria. La indentación del indicador de lista para los elementos de la lista anidada deben coincidir con el primer carácter del texto del elemento en la lista madre.
#. Lo máximo que se permiten son cuatro niveles de anidamiento, al menos si quieres exportar tu documento a PDF a través de Sphinx/LaTeX sin configuración adicional.

Primero que nada, el problema de una indentación arbitraria es que el texto se tomará como una cita/lista, lo que dependiendo del estilo puede resultar no agradable:

+ Primer nivel

    + Segundo nivel

El código en reStructuredText fue:

.. code-block:: rst

    + Primer nivel

        + Segundo nivel

Y generó lo siguiente en HTML:

.. code-block:: html

    <ul>
        <li><p>Primer nivel</p>
            <blockquote>
                <div>
                    <ul class="simple">
                        <li><p>Segundo nivel</p></li>
                    </ul>
                </div>
            </blockquote>
        </li>
    </ul>

.. raw:: latex

    \newpage

Por lo tanto, en este caso, el segundo nivel debe estar indentado dos espacios, para que el símbolo de la lista anidada esté alineado con la "P" inicial de la lista madre:

.. code-block:: rst

    + Primer nivel

      + Segundo nivel

En este caso, la lista se despliega adecuadamente, sin el bloque adicional de la cita:

+ Primer nivel

  + Segundo nivel

Y el HTML es mucho más limpio, como se espera:

.. code-block:: html

    <ul class="simple">
        <li><p>Primer nivel</p>
            <ul>
                <li><p>Segundo nivel</p></li>
            </ul>
        </li>
    </ul>

¿Y en qué afecta la presencia o ausencia de la línea en blanco? Eso depende. Visualmente en HTML, puede resultar casi lo mismo:

+ Primer nivel
    + Segundo nivel

Pero la lista sin la línea en blanco, es decir:

.. code-block:: rst

    + Primer nivel
        + Segundo nivel

En realidad genera el siguiente código en HTML:

.. code-block:: html

    <ul class="simple">
        <li><dl class="simple">
                <dt>Primer nivel</dt>
                <dd>
                    <ul><li><p>Segundo nivel</p></li></ul>
                </dd>
        </dl></li>
    </ul>

.. raw:: latex

    \newpage

Sea lo que sea, no estamos creando una lista simple (vale, es una lista de definiciones). En fin, el resumen sobre estas incongruencias es:

+ Si te pasas de espacios tendrás una lista dentro de una cita.
+ Si no pones una línea entre las listas tendrás una lista de deficiones.
+ Puede resultar tedioso hacer listas anidadas en reST si no se tiene cuidado.

Por último, lo de utilizar un máximo de cuatro niveles de anidamiento tiene que ver con su posible transformación a PDF a través de LaTeX. ¿Por qué? Porque LaTeX solo soporta solo cuatro niveles de anidamiento sin configuración adicional. Es decir, si tratas de generar un PDF de la siguiente lista

.. code-block:: rst
    :linenos:

    + Primer nivel

      + Segundo nivel

        + Tercer nivel

          + Podemos repetir

            + Indefinidamente

              + El símbolo por nivel

        * Regresamos al tercer nivel

      - Y al segundo

puede que recibas un error como:

.. code-block:: none

    LaTeX Error: Too deeply nested.

    See the LaTeX manual or LaTeX Companion for explanation.
    Type  H <return>  for immediate help.

    l.114 \begin{itemize}

Por supuesto, ese problema no ocurre en el `editor en línea <http://rst.ninjs.org/?theme=nature>`_, donde se puede visualizar el HTML con tantos niveles anidados de lista como se desee, y exportar el contenido a PDF (aunque eso se debe a que usa otra librería que no es LaTeX para su conversión). Como sea, no es algo que deba preocuparte mientras funcione.

.. raw:: latex

    \newpage

.. note::

    Aunque previamente dijimos que por nivel se debe usar un símbolo, el ejemplo anterior no genera advertencias. En teoría, deberíamos tener una advertencia por no utilizar el mismo símbolo para las líneas 5 y 13, y otra más gracias a 3 y 15. Dado que no es así, resta decir que para las personas que lleguemos a leer la fuente sigue siendo mejor. Trata de ser consistente.

¿Y qué pasa con el espacio en blanco?
"""""""""""""""""""""""""""""""""""""



Ah, sí, el espacio en blanco entre la viñeta y el texto es otro tema a no dejar pasar. Si no colocamos un espacio entre la viñeta y el texto, no se generará la lista. Por ejemplo, este texto:

+Primer elemento
+Segundo elemento

Sí, debió haber sido una lista... pero faltó dicho espacio entre símbolo y texto:

.. code-block:: rst

    +Primer elemento
    +Segundo elemento

No solo no se genera la lista, si en lugar de utilizar el símbolo **+** se hubiese utilizado la estrella, tendríamos una advertencia porque reST estaría buscando texto en itálicas:

.. code-block:: none

    WARNING: Inline emphasis start-string without end-string.

Por otro lado, si das uno o más espacios, siguen contando como uno solo:

.. code-block:: rst

    * Primer elemento
    *  Segundo elemento
    *    Tercer elemento

Da la siguiente lista:

* Primer elemento
*  Segundo elemento
*    Tercer elemento

Nótese que el espacio en blanco está entre el símbolo y el texto, y que no es indentación.



Listas con orden
^^^^^^^^^^^^^^^^



Las listas con orden se pueden crear con varios caracteres, aunque en este caso sí depende del carácter utilizado para la numeración que se dará (en el caso de las listas sin orden, todos los símbolos daban la misma viñeta).

La primer lista a describir es la compuesta por números arábigos:

1. Elemento.
2. Elemento.

Para crearla, simplemente utilizamos el número, seguido de un punto, un espacio, y luego el texto de cada elemento:

.. code-block:: rst

    1. Elemento.
    2. Elemento.

Otra forma de numeración aceptada es aquella que se hace con letras:

a. Elemento.
b. Elemento.

Y el código es:

.. code-block:: rst

    a. Elemento.
    b. Elemento.

Podemos realizar lo mismo, pero con las letras en mayúscula:

A. Elemento.
B. Elemento.

Cuyo código, que puedo jurar que intuyes, es el siguiente:

.. code-block:: rst

    A. Elemento.
    B. Elemento.

Y, por último, tenemos otros dos formatos gracias a los números romanos, igual en minúscula o mayúscula:

i. Romanos.
ii. Romanos.

IX. Romanos.
X. Romanos.

.. raw:: latex

    \newpage

Su código:

.. code-block:: rst

    i. Romanos.
    ii. Romanos.

    IX. Romanos.
    X. Romanos.



Paréntesis
""""""""""



Además de esas cinco formas de numeración, también puedes usar paréntesis para denotar la lista numerada. Por ejemplo:

.. code-block:: rst

    1. Hola.
    2. Adiós.

    1) Hola.
    2) Adiós.

    (1) Hola.
    (2) Adiós.

En HTML, las tres listas anteriores son equivalentes. En LaTeX, o mejor dicho la versión PDF con que se generó este libro, la salida sí varía:

1) Hola.
2) Adiós.



Uso de #
""""""""



No necesariamente tenemos que saber en qué número vamos. Podemos utilizar el carácter **#** para denotar "el siguiente elemento de la lista". Por ejemplo, las siguientes dos listas dan el mismo resultado:

.. code-block:: rst

    a) Primero
    b) Segundo

    a) Primero
    #) Segundo

Que se muestra como:

a) Primero
#) Segundo

En estos dos ejemplos, el primer elemento determina el estilo, mientras que los siguientes elementos se van calculando según se van imprimiendo.



Comenzando en otro número
"""""""""""""""""""""""""



En caso de querer empezar la numeración en otro número, es posible:

56. Elemento.
#. Elemento.
#. Elemento.

El código de la lista anterior es el siguiente:

.. code-block:: rst

    56. Elemento.
    #. Elemento.
    #. Elemento.

Donde podemos ver que el único número necesario es el inicial, cambiado a 56, y de allí reST puede seguir calculando con el uso del **#**. Este conteo y elemento inicial también aplica para los otros estilos, como el alfabético:

e. Primero
#. Segundo
#. Tercero

Donde la lista se realizó con el siguiente código:

.. code-block:: rst

    e. Primero
    #. Segundo
    #. Tercero

.. note::

    Una posible excepción notable en toda esta situación es una lista en números romanos comenzada en el número **v**. ¿Por qué? Resulta que reST asumirá que quieres hacer una lista alfabética que comienza en la **v**, por lo que sigue la **w**, por lo que la siguiente lista no se muestra adecuadamente:

    v. Quinto
    vi. Sexto
    vii. Séptimo

    El código desdichado es:

    .. code-block:: rst

        v. Quinto
        vi. Sexto
        vii. Séptimo



Sublistas
"""""""""



De maneras similar a las listas de viñetas, se puede crear listas anidadas al agregar indentación. Lo que es más, puedes combinar tantos estilos como quieras y puedas. De esto ya solo dejaremos un ejemplo:

1. Elemento arábigo 1.

   i. Elemento romano 1.
   #. Elemento romano 2.

      - Viñeta 1.
      - Viñeta 2.

   #. Elemento romano 3.

      c) Letras 3.
      #) Letras 4.

         A) Mayúsculas 1.
         #) Mayúsculas 2.
         #) Mayúsculas 3.

#. Elemento arábigo 2.

Cuyo código es:

.. code-block:: rst

    1. Elemento arábigo 1.

       i. Elemento romano 1.
       #. Elemento romano 2.

          - Viñeta 1.
          - Viñeta 2.

       #. Elemento romano 3.

          c) Letras 3.
          #) Letras 4.

             A) Mayúsculas 1.
             #) Mayúsculas 2.
             #) Mayúsculas 3.

    #. Elemento arábigo 2.



Diccionarios
^^^^^^^^^^^^



Un diccionario es un tipo de lista que se divide entre términos y sus definiciones. El formato de un diccionario consiste en el término sin sangría, y la definición indentada un nivel. Las definiciones lucen así:

primer término.
    Esta es la definición del primer término.
    Incluso si cambio de línea en la fuente, sigue estando en la misma línea de la definición.

segundo término.
    He aquí el 2do término, con su definición correspondiente.
tercer término.
    Poco importa el espacio entre definiciones.


cuarto término.
    Sin, o con uno o más saltos de línea, el resultado es el mismo.

Y el código para las definiciones pasadas es:

.. code-block:: rst

    primer término.
        Esta es la definición del primer término.
        Incluso si cambio de línea en la fuente, sigue estando en la misma línea de la definición.

    segundo término.
        He aquí el 2do término, con su definición correspondiente.
    tercer término.
        Poco importa el espacio entre definiciones.


    cuarto término.
        Sin, o con uno o más saltos de línea, el resultado es el mismo.

.. _texto-preformateado:

Texto preformateado (código fuente)
-----------------------------------



El texto preformateado es texto que no se convierte, aunque tenga símbolos de reStructuredText, y que preserva su espacio en blanco intacto. Se denota por el texto indentado después de una secuencia de dos símbolos de dos puntos (``::``), y una línea vacía, como sigue:

::

    ::

        Esto es código porque está indentado después de dos dos puntos.

Si no dejas la línea vacía entre los dos dos puntos y la primer línea de código, no se verá como tal:

::
    Esto debería ser código.
    Pero no lo es porque le faltó un salto de línea entre símbolos y texto.

Además, también funciona si colocas los dos dos puntos después de un párrafo, en cuyo caso se imprimen unos dos puntos en pantalla, y luego se inicia el bloque preformateado::

    Este bloque no empezó con una línea vacía con "::".

    El párrafo anterior terminó como "preformateado::",

    por eso se imprimieron los dos puntos.



Enlaces externos
----------------



Un enlace externo es un enlace que lleva a una dirección o sitio fuera de la propia documentación o el documento que estás realizando. Es decir, un enlace a cualquier URL que desees. Para Crear un enlace de este tipo podemos hacerlo de dos maneras: directa o indirectamente.



Enlace directo
^^^^^^^^^^^^^^



El enlace directo se coloca dentro del mismo texto. Para crear un enlace de esta manera se empieza con un acento grave (`````), seguido del texto del enlace, y entre signos de mayor que y menor que se coloca la URL, para finalizar con un acento grave y un guión bajo, como se muestra:

.. code-block:: rst

    `texto del enlace <url del enlace>`_

Por ejemplo, para ir al `sitio de Python <https://www.python.org/>`_ se utilizó el siguiente código:

.. code-block:: rst

    `sitio de Python <https://www.python.org/>`_



Enlace indirecto
^^^^^^^^^^^^^^^^

Si te parece que el texto con una URL embebida es difícil de leer puedes optar por crear un enlace mediante referencia (es decir, dividir el texto del enlace en dos).

Esto se hace agregando un guión bajo a una palabra. Por ejemplo, podemos crear un enlace mediante la palabra Python_ (escrita como ``Python_``). No obstante, al generar el documento obtendrás una advertencia:

.. code-block:: none

    WARNING: Unknown target name: "python".

.. raw:: latex

    \newpage

Y eso es porque ya definimos el texto del enlace, pero no su destino. Para definir la referencia escribimos dos puntos (``..``), espacio, guión bajo, la palabra que definimos previamente, seguida de un símbolo de dos puntos, y finalizamos con la URL:

.. code-block:: rst

    .. _Python: https://www.python.org/

También podemos usar un `conjunto de palabras`_ para crear un enlace, siempre y cuando las encerremos entre acentos graves y sigamos finalizando con el guión bajo:

.. code-block:: rst

    `conjunto de palabras`_

No obstante, para declarar la referencia no se necesitan los acentos graves:

.. code-block:: rst

    .. _conjunto de palabras: https://www.python.org/

Aquí cabe aclarar que la definición puede aparecer en cualquier parte del archivo, ya sea antes o después de donde la utilizamos, e igual el compilador la detecta. Lo recomendado es agrupar todas las definiciones de URL al final del documento. Por último, hay que decir que dicha definición es válida para múltiples instancias usando ese `conjunto de palabras`_ dentro del mismo documento.

A manera de recordatorio, he aquí la forma general de los enlaces indirectos, ya sean de una palabra o de varias:

.. code-block:: rst

    .. Se puede utilizar una sola palabra, sin acentos graves
    Palabra_
    .. Y declarar su referencia al final.
    .. _Palabra: pagina.com

    .. O bien un conjunto de palabras entre acentos graves
    `conjunto de palabras`_
    .. Definiendo la referencia sin acentos graves
    .. _conjunto de palabras: pagina.com



Enlaces internos
----------------



Los enlaces internos son referencias que nos llevan a contenido dentro de nuestro propio documento. De hecho, siguen la misma sintaxis que un enlace externo indirecto, pero sin definir la url:

.. code-block:: rst

    Texto para un `enlace interno`_

    Creación de la referencia del enlace interno:
    .. _enlace interno:

.. _enlace interno:

Es decir, puedes colocar el texto ``.. _enlace interno:`` en cualquier lugar de tu documento donde quieras crear un `enlace interno`_ (alguna nota importante, un término que quieras resaltar, o algún punto que consideres de particular interés... no aquí sobre este párrafo). Y, posteriormente, donde sea que lo quieras utilizar, mandarlo llamar con el texto entre acentos graves y con el guión bajo al final.



Enlaces implícitos
^^^^^^^^^^^^^^^^^^



Dado que algunos puntos de interés obvios dentro de nuestro documento son los títulos, reST los reconoce como enlaces internos implícitos. Es decir, puedo enlazar a secciones de este capítulo simplemente encerrando los títulos entre acentos graves y con su guión bajo, como `diccionarios`_, o `párrafos y líneas en blanco`_, o `comentarios`_.

Esos últimos tres enlaces no requirieron más código para su uso que el siguiente:

.. code-block:: rst

    como `diccionarios`_, o `párrafos y líneas en blanco`_, o `comentarios`_.

Recuerda: reST automáticamente te da acceso a los títulos para crear enlaces.



Tablas
------



Hay dos formas de hacer tablas en reST: una mala y otra peor. La verdad es que hacer tablas a partir de texto plano no puede ser agradable, no hay forma. Y reST no está solo en esto, es un problema compartido por HTML, Markdown, LaTeX, y cualquier otro lenguaje de marcado. Es en este momento donde se acepta la superioridad de la interfaz gráfica y se recomienda el uso de una, en la página `tablesgenerator.com`_. Gracias a ese generador podemos crear una hermosa tabla:

.. code-block:: rst

    +-------------------------+-------------+-------------+
    | Multicolumna            | Encabezado4 | Encabezado5 |
    +-----------+------+------+-------------+-------------+
    | Multifila | F2C2 | F2C3 | F2C4        | F2C5        |
    |           +------+------+-------------+-------------+
    |           | F3C2 | F3C3 | F3C4        | F3C5        |
    +-----------+------+------+-------------+-------------+
    | F4C1      | F4C2 | F4C3 | F4C4        | F4C5        |
    +-----------+------+------+-------------+-------------+

Ahora bien, según reST, el encabezado se marca con ``=`` debajo de la primera línea, por lo que tenemos que hacer este mínimo cambio para que se muestre como pretendemos:

.. code-block:: rst

    +-------------------------+-------------+-------------+
    | Multicolumna            | Encabezado4 | Encabezado5 |
    +===========+======+======+=============+=============+
    | Multifila | F2C2 | F2C3 | F2C4        | F2C5        |
    |           +------+------+-------------+-------------+
    |           | F3C2 | F3C3 | F3C4        | F3C5        |
    +-----------+------+------+-------------+-------------+
    | F4C1      | F4C2 | F4C3 | F4C4        | F4C5        |
    +-----------+------+------+-------------+-------------+


Y toda esa mezcla de ``-`` para separar filas, ``|`` para separar columnas, ``=`` debajo del encabezado, y ``+`` para las uniones nos da la siguiente tabla:

+-------------------------+-------------+-------------+
| Multicolumna            | Encabezado4 | Encabezado5 |
+===========+======+======+=============+=============+
| Multifila | F2C2 | F2C3 | F2C4        | F2C5        |
|           +------+------+-------------+-------------+
|           | F3C2 | F3C3 | F3C4        | F3C5        |
+-----------+------+------+-------------+-------------+
| F4C1      | F4C2 | F4C3 | F4C4        | F4C5        |
+-----------+------+------+-------------+-------------+

Ahora bien, hay otra forma "más sencilla" de hacer tablas, aunque no nos permite hacer multifilas. Este tipo de tabla solo requiere que las columnas tengan ancho fijo, por ejemplo:

================= =================
Encabezado1       Encabezado2
================= =================
Fila 2, Columna 1 Fila 2, Columna 2
Fila 3, Columna 1 Fila 3, Columna 2
================= =================

Para iniciar y terminar este tipo de tablas se requiere de líneas con símbolos de igual, separadas por espacios según las columnas que sean, y debajo del encabezado va otra igual. Fuera de esto, todas las columnas deben tener el mismo ancho y las columnas de iguales deben contenerlas:

.. code-block:: rst

    ================= =================
    Encabezado1       Encabezado2
    ================= =================
    Fila 2, Columna 1 Fila 2, Columna 2
    Fila 3, Columna 1 Fila 3, Columna 2
    ================= =================

En el momento que llegues a excederte en un elemento en alguna columna, tendrás una advertencia como la siguiente:

.. code-block:: rst

    WARNING: Malformed table.
    Text in column margin in table line 2.

    ================= =================
    Encabezado muy largo Encabezado2
    ================= =================

En este caso, el documento se generará sin rastro de tu tabla. Aunque, sí, es bastante simple este formato, un solo elemento que exceda tu largo de columna inicial implica que luego tengas que extender manualmente todos los anteriores para dar el ancho fijo adecuado.

En lugar de batallar, simplemente escucha mi consejo: utiliza `tablesgenerator.com`_, copia, pega, cambia la línea del encabezado, y sé feliz.



Resumen
-------



En este capítulo vimos la sintaxis de reST para componer texto de relativa complejidad. Vimos cómo se formaban los párrafo, la importancia de las líneas en blanco y la indentación, como colocar **\*\*negritas\*\*** y *\*cursivas\**, y cómo incluir títulos, listas, comentarios, y hasta enlace y tablas.

No obstante, con reST podemos lograr más cosas a través de directivas, nuestro tema del siguiente capítulo.



.. #######################################################################
.. ### Enlaces externos ##################################################
.. #######################################################################

.. _teoría de las ventanas rotas: https://es.wikipedia.org/wiki/Teor%C3%ADa_de_las_ventanas_rotas
.. _Python: https://www.python.org/
.. _conjunto de palabras: https://www.python.org/
.. _tablesgenerator.com: https://www.tablesgenerator.com/text_tables
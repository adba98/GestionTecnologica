var ruleta;
var winningSegment;
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var puntaje = 0;
var vidas = 3;
var preguntasA =[
    "La propiedad intelectual se compone de:","La propiedad intelectual se compone de:","La propiedad intelectual se compone de:"
];

var preguntasB =[
    "cual de los siguientes NO hace parte de los derechos de obtentor:","cual de los siguientes NO hace parte de los derechos de obtentor:","cual de los siguientes NO hace parte de los derechos de obtentor:"
];

var preguntasC =[
    "1C","2C","3C"
];

var preguntasD =[
    "1D","2D","3D"
];

var preguntasE =[
    "1E","2E","3E"
];

var respuestasA = [
    ["a1A","b1A","c1A","d1A"],
    ["a2A","b2A","c2A","d2A"],
    ["a3A","b3A","c3A","d3A"]
];

var respuestasB = [
    ["a1","b1","c1","d1"],
    ["a2","b2","c2","d2"],
    ["a3","b3","c3","d3"]
];

var respuestasC = [
    ["a1","b1","c1","d1"],
    ["a2","b2","c2","d2"],
    ["a3","b3","c3","d3"]
];

var respuestasD = [
    ["a1","b1","c1","d1"],
    ["a2","b2","c2","d2"],
    ["a3","b3","c3","d3"]
];

var respuestasE = [
    ["a1","b1","c1","d1"],
    ["a2","b2","c2","d2"],
    ["a3","b3","c3","d3"]
];

function DibujarRuleta() {
    ruleta = new Winwheel({
        'numSegments': 5,
        'outerRadius' : 170,
        'segments' : [
        { 'fillStyle': '#C39BD3', 'text': 'Tema a'},
        { 'fillStyle': '#85C1E9', 'text': 'Tema b'},
        { 'fillStyle': '#73C6B6', 'text': 'Tema c'},
        { 'fillStyle': '#F7DC6F', 'text': 'Tema d'},
        { 'fillStyle': '#EC7063', 'text': 'Tema e'},
        ],
        'animation' :{
            'type'          : 'spinToStop',
            'callbackFinished': 'Mensaje()',
            'callbackAfter': 'DibujarTriangulo()' ,
            'duration'      : 10,
            'spins'         : 5,
            'callbackSound' : playSound(),
            'soundTrigger'  : 'pin'
        },
        'pins' :{'number' : 16}
    });
    DibujarTriangulo();
}

let audio = new Audio("img/misc333.mp3");

function playSound(){
    alert("hola")
    audio.pause();
    audio.currentTime = 0;
    audio.play();
    audio.muted="muted"
}

function Mensaje() {
    winningSegment = ruleta.getIndicatedSegment();
    swal({
        title: " ¡ " + winningSegment.text + " !",
        imageUrl: "img/pi.png",
        confirmButtonColor: "#28B463",
        confirmButtonText: "Responder",
        closeOnConfirm: true
    },
        function (isConfirm) {
            if (isConfirm) {
                document.getElementById('girar').disabled= true;
                temaRuleta(winningSegment.text)
            }
            ruleta.stopAnimation(false);
            ruleta.rotationAngle = 0;
            ruleta.draw();
            DibujarTriangulo();
        });

}

function DibujarTriangulo() {
    ctx = ruleta.ctx;
    ctx.strokeStyle = 'navy';
    ctx.fillStyle = '#424949';
    ctx.beginPath();
    ctx.lineTo(210, 5);
    ctx.lineTo(200, 50);
    ctx.lineTo(185, 5);
    ctx.stroke();
    ctx.fill();
}

function temaRuleta(tema){
    switch (tema) {
        case 'Tema a':
            generarPregunta(preguntasA, respuestasA)
        break;
        case 'Tema b':
            generarPregunta(preguntasB, respuestasB)
        break;
        case 'Tema c':
            generarPregunta(preguntasC, respuestasC)
        break;
        case 'Tema d':
            generarPregunta(preguntasD, respuestasD)
        break;
        case 'Tema e':
            generarPregunta(preguntasE, respuestasE)
        break;
    }

}

function generarPregunta(preguntas,respuestas){
    var indice_aleatorio = Math.floor(Math.random()*preguntas.length);
    var respuestas_posibles = respuestas[indice_aleatorio];
    var posiciones = [0,1,2,3];
    var respuestas_reordenadas = [];

    var acierto = false;
    for(i in respuestas_posibles){
        var posicion_aleatoria = Math.floor(Math.random()*posiciones.length);
        if(posicion_aleatoria==0 && acierto == false){
            indicie_respuesta_correcta = i;
            acierto = true;
        }
        respuestas_reordenadas[i] = respuestas_posibles[posiciones[posicion_aleatoria]];
        posiciones.splice(posicion_aleatoria, 1);
    }

    var txt_respuestas="";
    for(i in respuestas_reordenadas){
        txt_respuestas += '<input type="radio" name="pp" value="'+i+'"><label>'+
        respuestas_reordenadas[i]+'</label>';
    }

    
    document.getElementById("respuestas").innerHTML = txt_respuestas;
    document.getElementById("pregunta").innerHTML = preguntas[indice_aleatorio];
    document.getElementById('btnResp').innerHTML = '<input id="resp" class="btn btn-color btn-success" type="button" value="Responder" onclick="comprobar();" />';

}

function comprobar(){
	var respuesta = $("input[type=radio]:checked").val();
	if(respuesta == indicie_respuesta_correcta){
        puntaje = puntaje + 10
        document.getElementById('puntaje').innerHTML = "<h3>" + puntaje +"</h3>";
	}else{
        vidas = vidas - 1
        if( vidas == 0){
            swal({
                title: " ¡ Ha Perdido !\n Puntaje: "+ puntaje,
                imageUrl: "img/pi.png",
                confirmButtonColor: "#e74c3c",
                confirmButtonText: "Reiniciar",
                closeOnConfirm: true
            },
                function (isConfirm) {
                    location.reload();
                });
        }
        document.getElementById('intentos').innerHTML = "<h3>" + vidas +"</h3>";
    }
    document.getElementById('girar').disabled= false;
    document.getElementById('resp').disabled= true;
}


DibujarRuleta();
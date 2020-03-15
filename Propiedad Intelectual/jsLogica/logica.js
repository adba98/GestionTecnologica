var ruleta;
var winningSegment;
var distnaciaX = 15;
var distnaciaY = 50;
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var img = new Image();
img.src = "img/pi.png";


ctx.drawImage(img, 100, 50);

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
        'animation' : {
            'type': 'spinToStop',
            'duration' : 5,
            'spins': 15,
            'callbackFinished': 'Mensaje()',
            'callbackAfter': 'DibujarTriangulo()' 
        }
    });
    DibujarTriangulo();
}

function Mensaje() {
    winningSegment = ruleta.getIndicatedSegment();
    swal({
        title: " ¡ " + winningSegment.text + " !",
        imageUrl: "img/pi.png",
        showCancelButton: true,
        confirmButtonColor: "#e74c3c",
        confirmButtonText: "Ok,Reiniciar",
        cancelButtonText: "Quitar elemento",
        closeOnConfirm: true,
        closeOnCancel: true
    },
        function (isConfirm) {
            if (isConfirm) {
                document.getElementById('puntaje').innerHTML = "H";
            } else {

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
    ctx.fillStyle = '#000000';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(distnaciaX + 170, distnaciaY + 5);
    ctx.lineTo(distnaciaX + 230, distnaciaY + 5);
    ctx.lineTo(distnaciaX + 200, distnaciaY + 40);
    ctx.lineTo(distnaciaX + 171, distnaciaY + 5);
    ctx.stroke();
    ctx.fill();
}

DibujarRuleta();
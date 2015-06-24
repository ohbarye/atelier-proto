var clock = new THREE.Clock();
$(document).ready(function(){
//  getJson("http://localhost:8000/atelier/api/artworks/?classId=n04584207&rankThres=1&scoreThres=0.5");

  getJson("http://52.68.196.235/atelier/api/artworks/?classId=n04584207&rankThres=1&scoreThres=0.5");
//  setup();
  animate();

});

var imagelist = [];
var objects = [];
var targets = {table: [], sphere: [], helix: [], grid: [], random: []};

var jsonData;
var nImage = 50;

var containerWidth, containerHeight;

function getJson(fileName){
    $.getJSON(fileName, function(data){

      jsonData = data;
      for(var i=0;i<nImage;i++){

        console.log(jsonData.album_list[i].album.artwork_url);
        imagelist.push(jsonData.album_list[i].album.artwork_url);
        //imagelist.push("../AlbumImage/"+data[i].imagePath);

      }

      //setBackgroundImage();
      setup();
      transform(targets.table, 2000);

    });

}

setTimeout(function(){

  setInterval(function(){

    var rotateImageNo = Math.floor(Math.random()*nImage);
    rotateImage(objects[rotateImageNo], 1000);


  }, 3000);

},5000);

function setup(){

  var container = document.createElement("div");

  //document.body.appendChild( container );
  var canvasArea = $("#rightPanel");
  canvasArea.append( container );

  containerWidth  = canvasArea.width();
  containerHeight = canvasArea.height();

  // camera
  camera = new THREE.PerspectiveCamera(40, containerWidth / containerHeight, 1, 15000);
  //camera = new THREE.PerspectiveCamera( 40, window.innerWidth / window.innerHeight, 1, 15000 );
  camera.position.z = 3000;

  // controls

//  controls = new THREE.OrbitControls( camera );

  // scene

  scene = new THREE.Scene();
  scene.fog = new THREE.Fog( 0x000000, 3500, 15000 );
  scene.fog.color.setHSL( 0.51, 0.4, 0.01 );

  // world

  var imageSize = 350;
  var plane = new THREE.PlaneGeometry(imageSize, imageSize);

  for(var i=0;i<nImage;i++){

    var imageTexture = THREE.ImageUtils.loadTexture(imagelist[i]);
    var material = new THREE.MeshBasicMaterial({
      map: imageTexture,
      side: THREE.DoubleSide
    });
    var mesh = new THREE.Mesh(plane, material);

    mesh.position.x = Math.random()*4000 - 2000;
    mesh.position.y = Math.random()*4000 - 2000;
    mesh.position.z = Math.random()*4000 - 2000;

    scene.add(mesh);
    objects.push(mesh);



    //
    var object = new THREE.Object3D();
    var x, y, z;
    var nImageInRow = 8;
    x = ((i%nImageInRow) * (imageSize+80)) - (imageSize+80)*nImageInRow/2 + (imageSize+80)/2;
    y = (- (Math.floor(i / nImageInRow))* (imageSize+80)) + (imageSize+80)*2;
    z = 0;

    object.position.x = x;
    object.position.y = y;
    object.position.z = z;

    targets.table.push(object);


  }


  // sphere
  for(var i=0;i<nImage;i++){

    var phi = Math.acos( -1 + ( 2 * i ) / nImage );
    var theta = Math.sqrt( nImage * Math.PI ) * phi;

    var object = new THREE.Object3D();

    var x, y, z;
    x = 800 * Math.cos( theta ) * Math.sin( phi );
    y = 800 * Math.sin( theta ) * Math.sin( phi );
    z = 800 * Math.cos( phi );

    object.position.x = x;
    object.position.y = y;
    object.position.z = z;

    var v = new THREE.Vector3();
    v.copy( object.position ).multiplyScalar(2);
    object.lookAt(v);

    targets.sphere.push(object);

  }


  // helix

  var vector = new THREE.Vector3();

  for ( var i = 0, l = nImage; i < l; i ++ ) {

    var phi = i * 0.175 + Math.PI;

    var object = new THREE.Object3D();

    object.position.x = 900 * Math.sin( phi );
    object.position.y = - ( i * 8 ) + 450;
    object.position.z = 900 * Math.cos( phi );

    vector.x = object.position.x * 2;
    vector.y = object.position.y;
    vector.z = object.position.z * 2;

    object.lookAt( vector );

    targets.helix.push( object );

  }

  // grid
  for ( var i = 0; i < nImage; i ++ ) {

    var object = new THREE.Object3D();

    object.position.x = ( ( i % 3 ) * 400 ) - 800;
    object.position.y = ( - ( Math.floor( i / 3 ) % 3 ) * 400 ) + 800;
    object.position.z = ( Math.floor( i / 9 ) ) * 1000 - 2000;

    targets.grid.push( object );

  }

  // random
  // for(var i=0; i<nImage;i++){
  //
  //   var object = new THREE.Object3D();
  //   object.position.x = Math.floor( Math.random )
  //
  // }


  // var imageTexture1 = THREE.ImageUtils.loadTexture("../AlbumImage/0000000710_350.jpg");
  // var material = new THREE.MeshBasicMaterial({
  //   map: imageTexture1
  // });
  // var mesh = new THREE.Mesh(plane, material);
  // mesh.position.x = 0;
  // mesh.position.y = 0;
  // mesh.position.z = 0;
  // scene.add(mesh);


  // lights

  // var ambient = new THREE.AmbientLight( 0xffffff );
  // ambient.color.setHSL( 0.1, 0.3, 0.2 );
  // scene.add( ambient );
  //
  //
  // var dirLight = new THREE.DirectionalLight( 0xffffff, 0.125 );
  // dirLight.position.set( 0, -1, 0 ).normalize();
  // scene.add( dirLight );
  //
  // dirLight.color.setHSL( 0.1, 0.7, 0.5 );


  // lens flares

  // var textureFlare0 = THREE.ImageUtils.loadTexture( "./lib/three-js/examples/textures/lensflare/lensflare0.png" );
  // var textureFlare2 = THREE.ImageUtils.loadTexture( "./lib/three-js/examples/textures/lensflare/lensflare2.png" );
  // var textureFlare3 = THREE.ImageUtils.loadTexture( "./lib/three-js/examples/textures/lensflare/lensflare3.png" );
  //
  //  //addLight(1.0, 1.0, 1.0, 0, 0, 10000 );
  // // addLight(1.0, 1.0, 1.0, 0, 0, -1000 );
  // // addLight( 0.08, 0.8, 0.5,    0, 0, -1000 );
  // // addLight( 0.995, 0.5, 0.9, 5000, 5000, -1000 );
  //
  // function addLight( h, s, l, x, y, z ) {
  //
  //   var light = new THREE.PointLight( 0xffffff, 1.5, 4500 );
  //   light.color.setHSL( h, s, l );
  //   light.position.set( x, y, z );
  //   scene.add( light );
  //
  //   var flareColor = new THREE.Color( 0xffffff );
  //   flareColor.setHSL( h, s, l + 0.5 );
  //
  //   var lensFlare = new THREE.LensFlare( textureFlare0, 700, 0.0, THREE.AdditiveBlending, flareColor );
  //
  //   lensFlare.add( textureFlare2, 512, 0.0, THREE.AdditiveBlending );
  //   lensFlare.add( textureFlare2, 512, 0.0, THREE.AdditiveBlending );
  //   lensFlare.add( textureFlare2, 512, 0.0, THREE.AdditiveBlending );
  //
  //   lensFlare.add( textureFlare3, 60, 0.6, THREE.AdditiveBlending );
  //   lensFlare.add( textureFlare3, 70, 0.7, THREE.AdditiveBlending );
  //   lensFlare.add( textureFlare3, 120, 0.9, THREE.AdditiveBlending );
  //   lensFlare.add( textureFlare3, 70, 1.0, THREE.AdditiveBlending );
  //
  //   lensFlare.customUpdateCallback = lensFlareUpdateCallback;
  //   lensFlare.position.copy( light.position );
  //
  //   scene.add( lensFlare );
  //
  // }

  // axis helper
  var axis = new THREE.AxisHelper(1000);
  scene.add( axis );

  // renderer

  renderer = new THREE.WebGLRenderer( { antialias: true, alpha: true } );
  renderer.setClearColor( 0x000000, 0 );
  renderer.setPixelRatio( window.devicePixelRatio );
  renderer.setSize( containerWidth, containerHeight );
  container.appendChild( renderer.domElement );

  //

  renderer.gammaInput = true;
  renderer.gammaOutput = true;

  // stats

  stats = new Stats();
  container.appendChild( stats.domElement );

  // events

  window.addEventListener( 'resize', onWindowResize, false );

  window.addEventListener( 'click', clickEvent, false);

}

function clickEvent(){

  runAwayFromWindow();
  setTimeout(function(){

    backToWindow();

  }, 1000);

}

function lensFlareUpdateCallback( object ) {

 var f, fl = object.lensFlares.length;
 var flare;
 var vecX = -object.positionScreen.x * 2;
 var vecY = -object.positionScreen.y * 2;


 for( f = 0; f < fl; f++ ) {

      flare = object.lensFlares[ f ];

      flare.x = object.positionScreen.x + vecX * flare.distance;
      flare.y = object.positionScreen.y + vecY * flare.distance;

      flare.rotation = 0;

 }

 object.lensFlares[ 2 ].y += 0.025;
 object.lensFlares[ 3 ].rotation = object.positionScreen.x * 0.5 + THREE.Math.degToRad( 45 );

}

//

function onWindowResize( event ) {

 renderer.setSize( window.innerWidth, window.innerHeight );

 camera.aspect = window.innerWidth / window.innerHeight;
 camera.updateProjectionMatrix();

}

//
function transform(targets, duration){

  TWEEN.removeAll();
  for(var i=0;i<nImage;i++){

    var object = objects[i];
    var target = targets[i];
    new TWEEN.Tween(object.position)
        .to({x: target.position.x, y:target.position.y, z:target.position.z}, Math.random()*duration + duration)
        //.easing(TWEEN.Easing.Linear.None)
        .easing(TWEEN.Easing.Exponential.InOut)
        .start();

    new TWEEN.Tween(object.rotation)
        .to({x: target.rotation.x, y:target.rotation.y, z:target.rotation.z}, Math.random()*duration + duration)
        //.easing(TWEEN.Easing.Linear.None)
        .easing(TWEEN.Easing.Exponential.InOut)
        .start();

    new TWEEN.Tween(this)
        .to({}, duration*2)
        .onUpdate(render)
        .start();

  }


}

//
function rotateImage(image, duration){

  var rotation = image.rotation;

  new TWEEN.Tween(image.rotation)
      .to({x: rotation.x, y: rotation.y + Math.PI*2, z:rotation.z}, duration)
      .easing( TWEEN.Easing.Linear.None )
      .start();

  new TWEEN.Tween(this)
      .to({}, duration)
      .onUpdate(render)
      .start();

}

//
function runAwayFromWindow(){

  for(var i=0;i<nImage;i++){

    var runAwayX, runAwayY;
    if(Math.random() > 0.5){

      if(Math.random() > 0.5){

        runAwayX = -1 * containerWidth*3;

      }
      else{

        runAwayX = containerWidth*3;

      }

      runAwayY = Math.random() * containerHeight*4 - containerHeight *2.;

    }
    else{

      if(Math.random() > 0.5){

        runAwayY = -1 * containerHeight*3;

      }
      else{

        runAwayY = containerHeight*3;

      }

      runAwayX = Math.random() * containerWidth * 4 - containerWidth * 2.;

    }


    new TWEEN.Tween(objects[i].position)
        .to({x: runAwayX, y: runAwayY, z:0}, 1000)
        .easing(TWEEN.Easing.Exponential.InOut )
        .start();

  }

  new TWEEN.Tween(this)
      .to({}, 1000)
      .onUpdate(render)
      .start();

}

//
function backToWindow(){

  transform(targets.table, 2000);

}

//

function animate() {

 requestAnimationFrame( animate );

 TWEEN.update();

 render();
 stats.update();

}

function render() {

 var delta = clock.getDelta();

// controls.update( delta );
// renderer.render( backgroundScene, backgroundCamera );
 renderer.render( scene, camera );

}

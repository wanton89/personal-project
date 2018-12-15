(function() {

    const preObject = document.getElementById('object');

    const dbRefObject = firebase.database().ref().child('object);

    dbRefObject.on('value', snap => {
        preObject.innerText = JSON.stringify(snap.val(), null, 3);
    });

}());




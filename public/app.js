(function() {


    var database = firebase.database().ref('tests');
    database.once('value', function(snapshot) {
        console.log(snapshot.val());
    });
}());




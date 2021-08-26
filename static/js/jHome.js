
// This will tell you the hostname and port of the page
console.log(window.location.host);

// Example of simple GET request using Ajax to get Username
$.ajax({
    'method': 'GET',
    'url': '/getUserName',
    'content-type': 'application/json',
    'success': function(response) {
        // Frontend (200) Success

        if (response['status'] === 'Success') {
            // Backend Success Response
            console.log(response);
            $('.user_name').text(response['data']['name']);
        
        } else if (response['status'] === 'Fail') {
            // Backend Failed Response
            console.log(response['err'])
        }
    },
    'error': function(error) {
        // FrontEnd (400 Errors) will go here
        console.log(error);
    }
});

// .off() -Is used to reset jQuery's internal counter so it doesnt run the function multiple times
// .on() - You can specify which element to look at

// GET Request with ajax to load Friends onto Page
$('.loadFriends').off().on('click', function() {
    $.ajax({
        'method': 'GET',
        'url': '/getFriendsList',
        'content-type': 'application/json',
        'success': function(response) {

            if (response['status'] === 'Success') {
                console.log(response);
                    
                for (var i=0; i < response['data']['friends'].length; i++) {
                    $('.friendsList').append("<li>" + response['data']['friends'][i]['username'] + "</li>");   
                }
            
            } else if (response['status'] === 'Fail') {
                console.log(response['err']);
            }

        },
        'error': function(error) {
            console.log(error);
        }
    });

});


// POST Request with ajax to save a new friend
$('.newFriend').off().on('click', function() {
    $('.form').css({'display':'flex'});
});

$('.submitBtn').off().on('click', function() {
    
    // Retrieve the values from the form and put it into one dictionary
    var data = {
                'name': $('#name').val(),  
                'age': $('#age').val(),  
                'email': $('#email').val(),  
                };
    
    console.log(data);

    $.ajax({
        'method': 'POST',
        'url': '/addFriend',
        'content-type': 'application/json',
        'data': JSON.stringify(data),
        'success': function(response) {

            if (response['status'] === 'Success') {
                console.log(response);
                alert('SUCCESS FRIEND ADDDED!');
            } else if (response['status'] === 'Fail') {
                console.log(response['err']);
            }

        },
        'error': function(err) {
            console.log(error);
        }
    });

    
});
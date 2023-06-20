$('#predictBtn').click(function() {
    var heartRate = $('#heartRate').val();
    var restingHeartRate = $('#restingHeartRate').val();
    var bmi = $('#bmi').val();
    var calories = $('#calories').val();
    var age = $('#age').val();
    var gender = $('#gender').val();
    
    // Create the form data object
    var formData = {
        heartRate: heartRate,
        restingHeartRate: restingHeartRate,
        bmi: bmi,
        calories: calories,
        age: age,
        gender: gender
    };
    
    // Make the AJAX request
    $.ajax({
        url: '/predict',
        type: 'POST',
        data: JSON.stringify(formData), // Convert the data to JSON format
        contentType: 'application/json', // Set the content type to JSON
        dataType: 'json', // Set the expected response type to JSON
        success: function(response) {
            // Handle the successful response
            console.log(response);
        },
        error: function(error) {
            // Handle the error
            console.log(error);
        }
    });
});

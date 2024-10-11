document.addEventListener('DOMContentLoaded', function() {

    // Calorie Tracking
    document.getElementById('add-calorie-btn').addEventListener('click', function() {
        const calorieInput = document.getElementById('calorie-input').value;
        if (calorieInput) {
            const listItem = document.createElement('li');
            listItem.textContent = `${calorieInput} kcal`;
            document.getElementById('calorie-list').appendChild(listItem);
            document.getElementById('calorie-input').value = ''; // Clear input
        } else {
            alert('Please enter calorie value!');
        }
    });

    // Sleep Tracking
    document.getElementById('add-sleep-btn').addEventListener('click', function() {
        const sleepInput = document.getElementById('sleep-input').value;
        if (sleepInput) {
            const listItem = document.createElement('li');
            listItem.textContent = `${sleepInput} hours of sleep`;
            document.getElementById('sleep-list').appendChild(listItem);
            document.getElementById('sleep-input').value = ''; // Clear input
        } else {
            alert('Please enter sleep duration!');
        }
    });

    // Habit Tracking
    document.getElementById('add-habit-btn').addEventListener('click', function() {
        const habitInput = document.getElementById('habit-input').value;
        if (habitInput.trim()) {
            const listItem = document.createElement('li');
            listItem.textContent = habitInput;
            document.getElementById('habit-list').appendChild(listItem);
            document.getElementById('habit-input').value = ''; // Clear input
        } else {
            alert('Please enter a habit!');
        }
    });

    // Fitness Tracking
    document.getElementById('add-workout-btn').addEventListener('click', function() {
        const workoutType = document.getElementById('workout-type').value;
        const workoutDuration = document.getElementById('workout-duration').value;
        if (workoutType && workoutDuration) {
            const listItem = document.createElement('li');
            listItem.textContent = `${workoutType} - ${workoutDuration} minutes`;
            document.getElementById('workout-list').appendChild(listItem);
            document.getElementById('workout-type').value = '';
            document.getElementById('workout-duration').value = '';
        } else {
            alert('Please enter workout type and duration!');
        }
    });

});

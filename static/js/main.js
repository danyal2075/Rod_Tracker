/**
 * Updates the current color, distance and motor status calling teh corresponding methods
 */
function updateStatus() { console.log('qrqrqwerewrqewr')
  // Update current color based on Open CV
  updateCurrentColorOpenCV()
  
  // Update motor status
  //...
  
  // Update current color based on distance sensor
  //...

  // Update current distance
  //...
}

/**
 * Update the current color based on OpenCV
 */
 async function updateCurrentColorOpenCV() {
  try {
    // Request color from server
    const requestResult = await requestColorFromOpenCV()
    // Get the HTML element where the status is displayed
    const green_open_cv = document.getElementById('green_open_cv')
    green_open_cv.innerHTML = requestResult.data[0]
    const purple_open_cv = document.getElementById('purple_open_cv')
    purple_open_cv.innerHTML = requestResult.data[1]
    const yellow_open_cv = document.getElementById('yellow_open_cv')
    yellow_open_cv.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    updateStatus('Error getting the color based on OpenCV')
  }
}


var requestResult = { data :[]}

/**
 * Function to request the server to update the current color based on OpenCV
 */
 function requestColorFromOpenCV () {
  try {
    // Make request to server
     var res = axios.get('/get_color_from_opencv');
     console.log(12,res)
    return res
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Function to request the server to start the motor
 */
 function requestStartMotor () {
  //...
}


/**
 * Function to request the server to stop the motor
 */
function requestStopMotor () {
  //...
}

/**
 * Update the status of the motor
 * @param {String} status 
 */
 function updateMotorStatus(status) {
  // Get the HTML element where the status is displayed
  // ...
}

/**
 * Update the current color based on distance sensor
 */
 function updateDistance() {
  // Get the HTML element where the status is displayed
  try {
    // Request color from server
    const requestResult = await requestDistance()
    // Get the HTML element where the status is displayed
    const rod_distance = document.getElementById('rod_distance')
    rod_distance.innerHTML = requestResult.data[0]
   
  } catch (e) {
    console.log('Error getting the color based on distance', e)
    updateStatus('Error getting the color based on distance')
  }
}

var requestResult = { data :[]}
/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor
 */
function requestDistance () {
  try {
    // Make request to server
     var res = axios.get('/get_distance');
     console.log(12,res)
    return res
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Update the current color based on distance sensor
 */
 function updateCurrentColorDistance() {
  // Get the HTML element where the status is displayed
  try {
    // Request color from server
    const requestResult = await requestColorFromDistance()
    // Get the HTML element where the status is displayed
    const green_distance = document.getElementById('green_distance')
    green_distance.innerHTML = requestResult.data[0]
    const purple_distance = document.getElementById('purple_distance')
    purple_distance.innerHTML = requestResult.data[1]
    const yellow_distance = document.getElementById('yellow_distance')
    yellow_distance.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on distance', e)
    updateStatus('Error getting the color based on distance')
  }
}

var requestResult = { data :[]}
/**
 * Function to request the server to get the color based
 * on distance only
 */
function requestColorFromDistance () {
  try {
    // Make request to server
     var res = axios.get('/get_color_from_distance');
     console.log(12,res)
    return res
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}
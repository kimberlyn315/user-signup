<!DOCTYPE html>
     
     <div class="container">
        
        <h1>User Sign Up</h1>
         
    <div class="container">
        <form action="/action_page.php">
        <label for="usrname">Username</label>
        <input type="text" id="usrname" name="usrname" required>

        <label for="psw">Password</label>
        <input type="password" id="psw" name="psw" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{3,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 3 or more characters" required>

        <input type="submit" value="Submit">
        </form>
    </div>

    <div id="message">
        <h3>Password must contain the following:</h3>
        <p id="letter" class="invalid">A <b>lowercase</b> letter</p>
        <p id="capital" class="invalid">A <b>capital (uppercase)</b> letter</p>
        <p id="number" class="invalid">A <b>number</b></p>
        <p id="length" class="invalid">Minimum <b>3 characters</b></p>
    </div> 

        <label>
            <input type="checkbox" checked="checked" name="remember" style="margin-
            bottom:15px"> Remember me
        </label>
       
        <div class="clearfix">
            <button type="button" class="cancelbtn">Cancel</button>
            <button type="submit" class="signupbtn">Sign Up</button>
        </div>
    </div>

 


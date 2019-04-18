<!DOCTYPE html>
    <div class="container">
        <h1>User Sign Up</h1>
    </div>
    
    <div class="container">
        <form action="/action_page.php">
        <label for="usrname">Username</label>
        <input type="text" id="usrname" name="usrname" required>

        <label for="psw">Password</label>
        <input type="password" id="psw" name="psw" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{3,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 3 or more characters" required>

        <input type="submit" value="Submit">
        </form>
    </div>

    <label>
        <input type="checkbox" checked="checked" name="remember" style="margin-
        bottom:15px"> Remember me
    </label>
       
    <div class="clearfix">
        <button type="button" class="cancelbtn">Cancel</button>
        <button type="submit" class="signupbtn">Sign Up</button>
    </div>


 


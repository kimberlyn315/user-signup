
    <!DOCTYPE html>
     <div class="container">
        <h1>User Sign Up</h1>
         <p>Please fill in this form to create an account.</p>
        <hr>

        <label>Username: <input type="text" name="username"/></label>
        <input type="text" placeholder="Enter Username" name="username" required>
        <label style="color:red">{username_message}</label>
           
        <label for="psw"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" name="psw" required>
        <label style="color:red">{password_message}</label>
            
        <label for="psw-repeat"><b>Repeat Password</b></label>
        <input type="password" placeholder="Repeat Password" name="psw-repeat"
        required>
        <label style="color:red">{password_message}</label>

        <label>
            <input type="checkbox" checked="checked" name="remember" style="margin-
            bottom:15px"> Remember me
        </label>
       
        <div class="clearfix">
            <button type="button" class="cancelbtn">Cancel</button>
            <button type="submit" class="signupbtn">Sign Up</button>
        </div>
    </div>

 


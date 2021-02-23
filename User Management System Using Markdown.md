<!--Correct username: invitado / pass: hgm2015-->
  <button style='color:Blue' align = 'right' id="submit"> Save User</button> 

<section class="form animated flipInX">
    
  <h2> New User</h2>
  <form class="loginbox" autocomplete="off">
      
  <input placeholder="Username" type="text" id="username"></input>
  <br><br> 
  <input placeholder="Display Name" type="text" id="displayname"></input>
    
   <input placeholder="Phone" type="text" id="phone"></input>                             
    
   <input placeholder="Email" type="email" id="email"></input>
    
   <input type="checkbox" id="enabled" name="enabled" value="Enabled">
    <label for="enabled">Enabled</label><br>
    
    
   <label for="UserRoles">Select User Roles:</label>
  <select name="roles" id="roles">
    <option value="guest">Guest</option>
    <option value="admin">Admin</option>
    <option value="SuperAdmin">SuperAdmin</option>
  </select>
  <br><br>
  <button style='color:Blue' id="submit"> + New User</button> 
 <input type="checkbox" disabled checked> Hide Disabled User
 
| ID              | User Name    | Email                 | Enabled        |
|-----------------|:-------------|:---------------:       |---------------:|
| 1               | Admin Usser  | admin@piworks.net      | true           |
| 2               | Test User    | testuser@piworks.net   | true           |

</form>
</section>



```python

```

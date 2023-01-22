# **Task 1: Software Configuration**

### Subtask 1: Why did I choose to participate in the _**Dare IT Challenge**_?

Hello! My name is _**Mariya-Roksolyana**_ and I love manual testing!😃 
You might wonder why did I choose to participate in the _Automated_ Testing challenge then?
Well...because I also like to challenge myself😅 As simple as that! 
My _goal_ for this challenge is to learn as much as possible from knowledgeable experts 
and to get a grasp on what it takes to automate tests💪 
Not only will it help me expand my professional skills, but also give me a chance to apply 
for some better-paying jobs in the future (at least I hope so!)😊

Anyway, I am looking forward to what this experience has in store for me and I wish good luck 
to all my fellow participants!😉

# **Task 2: Selectors**

### Subtask 1:Searching for the selectors on the _Login page_

1. "Scouts Panel" title
 * //*[@id="__next"]/form/div/div[1]/h5
 * //*[text()="Scouts Panel"]
 * //*[contains (@class,"MuiTypography-root MuiTypography")]
2. "Login" input field
 * //*[@id="login"]
 * //input[@name="login" and @aria-invalid="false"]
 * //*[@type="text" and @id="login" and @name="login"]
3. "Password" input field
 * //*[@id="password"]
 * //*[contains (@name,"password")]
 * //*[contains (@name,"password") and contains (@id,"password")]
4. "Remind password" hyperlink
 * //*[@id="__next"]/form/div/div[1]/a
 * //*[contains (@tabindex, -1)]
 * //*[contains(@class,"MuiLink-underlineHover")]
5. Dropdown button for the language choice
 * //*[@id="__next"]/form/div/div[2]/div/div
 * //*[@role="button" and @aria-haspopup="listbox"]
 * //*[text()="English" and @role="button"]
6. "SIGN IN" button
 * //*[@id="__next"]/form/div/div[2]/button
 * //button[@type="submit"]
 * //*[text()="Sign in"]

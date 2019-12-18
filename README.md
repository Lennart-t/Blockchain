### HSG Diploma verification system

Group project by Laurens Hamm, Jonas Hansjosten and Lennart Teuber as part of the "Skills:  Programming with Advanced Computer Languages" course during the Fall Semester 2019 at the University of St. Gallen.

We have developed a *HSG diploma verification system*: a simple blockchain implementation in the form of a decentralized app (dAPP) that allows you to add new graduates and verify existing diplomas. In addition, we have implemented a block verification mechanism, which enables you to test the validity of each block to check against manipulation.

Our project includes a Back End, which we developed using Python and a Front End based on Python's Flask and a HTML-structure. For the main functionalities we followed a guide from [Anton Tarasov](https://u.today/how-to-build-a-blockchain-application-with-python). 

Our dApp exists of one index-site, which contains the main menu with links to all three functions and their respective sites 1) Add a graduate, 2) Verify a diploma, 3) Verify entire blockchain. From all functions sites there is a button implemented to go back to the main menu.

#### Overview of functionalities of those three sites:

<details>
<summary>1) Add a graduate</summary>
  
This page has five input fields (University key, Graduate name, Date of birth, Study  programm, Date of graduation). The University key is 12345. It is to ensure, that only HSG officials can add new graduates. Despite the field "Graduate name", which is unrestricted, all other fields can be filled by choosing values from the drop-down list. A new block in the chain will be created by clicking on the button "Submitting Graduation", if all fields are filled. If not, an error message will occur.
</details>

<details>
<summary>2) Verify a diploma</summary>
  
This page allows everyone to check, if the respective person has actually a HSG Diploma. Therefore same input fields must be filled compared to the "Add a graduate site". Only the "University key" is not needed. By clicking on Check Diploma all currently existing blocks will be checked for the entered information.
</details>

<details>
<summary>3) Verify entire blockchain</summary>
  
This page enables users to check, if any blocks were manipulated and therefore the blockchain is corrupted. It shows the status of all blocks. The status can be "genuine" (not manipulated) or "fake" (manipulated).
</details>


#### How to use our HSG diploma verification system:
1) Download the ZIP from Github.
2) Open the File in the ZIP in your virtual environment (do not change the folder structure and names to ensure compatibility).
3) Run main.py and open your localhost.

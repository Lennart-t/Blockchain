### HSG Diploma verification system

Group project by Laurens Hamm, Jonas Hansjosten and Lennart Teuber as part of the "Skills:  Programming with Advanced Computer Languages" course during the Fall Semester 2019 at the University of St. Gallen.

We have developed a *HSG diploma verification system*: a simple blockchain implementation in the form of a decentralized app (dAPP) that allows you to add new graduates and verify existing diplomas. In addition, we have implemented a block verification mechanism, which enables you to test the validity of each block to check against manipulation.

Our project includes a back-end, which we developed using Python and a front-end based on Python's Flask extension and a HTML-structure and mark-up. For the main functionalities, we followed a guide from [Anton Tarasov](https://u.today/how-to-build-a-blockchain-application-with-python). 

Our dApp exists of an index-site, which contains the main menu with links to all three functions and their respective sites 1) Add a graduate, 2) Verify a diploma, and 3) Verify entire blockchain. On all pages there is a button implemented to go back to the main menu.

#### Overview of functionalities of those three sites:

<details>
<summary>1) Add a graduate</summary>
  
This page has five input fields (University key, Graduate name, Date of birth, Study  programm, Date of graduation). The University key is 12345, which ensures that only HSG officials can add new graduates. The input fields can be filled by choosing values from the drop-down list, except for the field "Graduate name", which is unrestricted. If all fields are filled in correctly, a new block in the chain will be created by clicking on the button "Submitting Graduation". If the input is not correct, an error message will occur.
</details>

<details>
<summary>2) Verify a diploma</summary>
  
This page allows everyone to check, if the respective person actually has a HSG Diploma. Therefore, the same input fields must be filled compared to the "Add a graduate site". Only the "University key" is not needed. By clicking on "Check Diploma", all currently existing blocks will be checked for consistency of information.
</details>

<details>
<summary>3) Verify entire blockchain</summary>
  
This page enables users to check, whether any blocks were manipulated and therefore the blockchain is corrupted. It shows the status of all blocks. The status can be "genuine" (not manipulated) or "fake" (manipulated) or "unverifiable" in case it is the last block.
</details>


#### How to use our HSG diploma verification system:
1) Download the ZIP from Github.
2) Open the File in the ZIP in your virtual environment (please do not change the folder structure and names to ensure compatibility).
3) Run main.py and open your localhost.

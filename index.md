# Fast github action

### FAST Approaches to Scalable Similarity-based Test Case Prioritization

This repository is a "fork" of https://github.com/brenomiranda/FAST.
Fast is a tool which does test case priorizations. Given a test suitethe tool will do a priorization  by pairwise and return the test suite ordered by the algorithm

### FAST publication
> Breno Miranda, Emilio Cruciani, Roberto Verdecchia, and Antonia Bertolino. 2018. FAST Approaches to Scalable Similarity-based Test Case Prioritization. In *Proceedings of ICSE’18: 40th International Conference on Software Engineering, Gothenburg, Sweden, May 27-June 3, 2018 (ICSE’18)*, 11 pages. DOI: [10.1145/3180155.3180210](http://dx.doi.org/10.1145/3180155.3180210)

### Github action

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.


### The Fast Action
This action use the FAST project to to the priorization technique in whatever Junit project on a github repository.
The fast project has different algorithms and parameters. In this action fast will be running usins "FAST-PW" and will use the blackbox configuration, since in this action the fast will have access to the source code

### How it works ?
Basically, the action works following these steps:
    * Gets all java test files with the patter **Test.java and **_Test.java
    * Minify the collected classes into a one line
    * Send the processed classes to Fast
    * The action will write the ordered classes into **results.txt** at the root of the repository

### Getting started

1 -  Get the release to yout machine [download release](https://github.com/BigMilts/FAST_PRIVATE/archive/refs/tags/fast_action_v1.tar.gz)
2 -  Extract the .zip
3 -  Copy the *script* folder to your repository and put in the root
4 -  If you already have a workflow .yml file configurated on your project, you just need to add the job in the jobs tag
```markdown
jobs:
  #job1:
    # stpes...
  #job2:
    #steps...
  # Add this *private_fast_action job block at your jobs block
  private_fast_action:
    runs-on: ubuntu-latest
    name: Setup
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install scipy xxhash
      - name: RUN FAST
        run: python script/prioritize.py > results.txt
      - name: Setup git
        run: |
          git config user.name "FAST ACTION"
          git config user.email "<>"
      - name: Commit
        run: |
          git add results.txt
          git commit -m "persisting test data"
          git push
```
Nevertheless, if don't, you'll need to create a folder and a file with this pattern: **.github/workflows/<your_action_name>.yml**. Then, you must put in the file

```markdown

# This is a sample of action, if youi need more information, consult the 
https://docs.github.com/pt/actions/quickstart

name: Private Fast action
on:
  # define the event which will trigger the action
  push:
  # define the branch which you want the job to run
    branches: ['main']

jobs:
  private_fast_action:
    runs-on: ubuntu-latest
    name: Setup
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install scipy xxhash
      - name: RUN FAST
        run: python script/prioritize.py > results.txt
      - name: Setup git
        run: |
          git config user.name "FAST ACTION"
          git config user.email "<>"
      - name: Commit
        run: |
          git add results.txt
          git commit -m "commit messsage"
          git push
```


### Expected Restuls
There are 2 possibles results in the generated **results.txt** file.
1 - The content will be the test classes name ordered by Fast, in case the tests are following the Junit name convention.
2 - The content will be "No java test files in this repository" if there is no Junit java test files in your repository or it may happen if the files are not in the Junit name pattern.


Directory Structure
---------------
This is the root directory of the repository. The directory is structured as follows:

    FAST_PRIVATE
     .
     |
     |--- .github/workflows/        Holds this repository action.
     |
     |--- script/                   Implementation of the algorithms and scripts to execute the action.
     |
     |--- workflow_tempalte/        Holds the fast action template to be used in the others .yml files
     
 ## *Collaborators in the development of this action*

<table>
  <tr>
    <td align="center"><a href="https://github.com/mam81"><img src="https://avatars.githubusercontent.com/u/49957062?v=4" width="100px;" alt="Matheus Antunes"/><br /><sub><b>Matheus Antunes</b></sub></a><br /><a href="https://github.com/mam81">
    <td align="center"><a href="https://github.com/BigMilts"><img src="https://avatars.githubusercontent.com/u/51926931?v=4" width="100px;" alt="Milton Souto Maior"/><br /><sub><b>Milton Souto Maior</b></sub></a><br /><a href="https://github.com/BigMilts">
	<td align="center"><a href="https://github.com/RafaelNAIP"><img src="https://avatars.githubusercontent.com/u/51056390?v=4" width="100px;" alt="Rafael Dias"/><br /><sub><b>Rafael Dias</b></sub></a><br /><a href="https://github.com/RafaelNAIP">
    <td align="center"><a href="https://github.com/vitorlms"><img src="https://avatars.githubusercontent.com/u/54985552?v=4" width="100px;" alt="Vítor Lopes"/><br /><sub><b>Vítor Lopes</b></sub></a><br /><a href="https://github.com/vitorlms"></
  </tr>
</table>

Explaining the process
1. Create GitHub repository 
2. Create directory .github and workflows
3. Creating a yml file
4. On this file a wrote:
    - name task "Run tests"
    - This task will run when I push or pull request on branch master
    - Nest I define the jobs 
    - The job is to run tests, and makes sure that they run on ubuntu
    - how to job is done is defined by steps, 
      I cannot run the test without defining what my test need to run on.
    - first is to set workflow on GitHub
    - And den setup python with the correct version
    - next is to install poetry
    - we also need to install dependencies
    - Last but not least with run the test 
5. I made a toml file using poetry init on terminal 
6. I followed the step the terminal provides and added pytest as dependencies
7. Commit all my changes and seeing on GitHub action that the tests are run 
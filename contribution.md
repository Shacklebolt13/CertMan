# Contributing

If you have any idea to enhance the project and you would like to contribute or any fixes you want to contribute, be sure to follow this guideline.

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Important Notes

1. Issues that have the label `first-timers-only` is made for beginners who have contributed to less than 5 repositories. This is a way to help people who are new to open source and contributing.
2. Before contributing to an issue, make sure that no one is assigned or has taken that issue. If no one is and you would like to work on the issue, please comment on the issue to let others know that someone is working on the issue.
3. Before creating a pull request, it is **important** that you make sure your branch and repository are up to date with this one. Some conflicts can be resolved, but many are hard to resolve. **Add the upstream** branch and always keep your branch up to date.

# Contents

- [Contributing](#contributing)
  - [Important Notes](#important-notes)
- [Contents](#contents)
- [Instructions](#instructions)
  - [Create Pull Request](#create-pull-request)
    - [Note on abandoned pull requests](#note-on-abandoned-pull-requests)
  - [Code of Conduct](#code-of-conduct)
    - [Our Pledge](#our-pledge)
    - [Our Standards](#our-standards)
    - [Our Responsibilities](#our-responsibilities)
    - [Scope](#scope)
    - [Enforcement](#enforcement)

# Instructions

1. Fork the repository.

2. Make sure you are pushing changes which are assigned to you in Issues section.

3. Do the needful changes 

4. Review changes in VS Code Source Control

5. Push Changes
   
## Create Pull Request

1. Create a new branch:
   ```
   git branch new-branch
   ```
2. Checkout new branch:
   ```
   git checkout new-branch
   ```
3. Add, commit and push your changes to the new branch
   ```
   git add .
   git commit -m "Commit message with issue lable"
   git push origin new-branch
   ```
4. To make sure your forked repository is up to date with this repository. Add this repository as the upstream repository by doing the following:

```
git remote add upstream https://github.com/Shacklebolt13/CertMan.git

```

Then, to fetch from this repository:

```
git fetch upstream
git merge upstream/master master
```

5. Go to your forked repository and press the “New pull request” button.
6. Once the pull request is reviewed and approved, it will be merged.

### Note on abandoned pull requests

If a pull request is left unchanged for a week after changes are requested and the issue was assigned to the person that sent the new pull request, they will be unassigned and someone else will be given the chance to work on it.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or
  advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.
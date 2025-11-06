# LinkedIn Learning Codespaces Template

Version 1.0.0

Baseline template for creating exercise files for LinkedIn Learning courses. 

## How to use this template

1. Create a new repo using this template
2. Name the new repo according to the spec provided by your CM or producer
3. Configure the devcontainer to match your exercise file requirements
4. Add additional VS Code settings when necessary
5. Build out the exercise files as normal
6. Record your course using the template in Codespaces (unless otherwise agreed upon by your CM)
7. Update `README.md` to match your project
8. Update `NOTICE`
9. Delete the `/INSTRUCTOR_INSTRUCTIONS/` folder and its contents
10. Submit the finished exercise files repo to your producer

## Why we use this template

When the learner goes hands-on with your course they should experience a one-to-one match between the coding environment they see in the course and the one they work in on their computer.

We use GitHub Codespaces to ensure you're recording with the same environment the learner experiences. Using this template, your exercise files repo will include a customized devcontainer defining the exercise files environment and VS Code configuration ensuring visual and feature consistency.

_NOTE: If you cannot use GitHub Codespaces or need to use a different editor or tool to record your course, please talk to your CM before recording._

### Tips:
- Use this template to build the ideal development environment for your course
- Automate any prerequisite setup steps and other configurations either implied or not within the scope and learning goals of the course
- Use GitHub Models unless there is an explicit reason not to
- The goal is for the learner to drop right into the project and follow along without having to do any extra work!

## Core features

The template provides the starting point for you to configure the ideal environment for your course. Customize the environment to fit your course while keeping the visual elements (theme, font size, etc) intact.

Below is a detailed breakdown of the customization features and how to use them:

### Development Container

The template uses a development container (aka "devcontainer") to set up and configure Codespaces. Out of the box the devcontainer loads an image of a default linux environment, loads the LinkedIn Learning VS Code theme, opens the `README.md` file in the editor, configures the console to use `bash`, and syncs all forks from the origin repo.

You are free to edit the devcontainer to fit your needs provided you include the LinkedIn Learning theme under extensions.

`./.devcontainer/devcontainer.json` runs automatically on first load in GitHub Codespaces. Configure it to create the ideal environment for your course, including adding language support, installing dependencies, running scripts and automation processes, opening ports, rendering files, etc. 

[You can further control the devcontainer environment by adding a `Dockerfile`.](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#dockerfile)

#### Devcontainers in-depth
- Use the [`image` property](https://containers.dev/implementors/json_reference/#image-specific) to load the default image or a custom image from DockerHub, GitHub Container Registry, or Azure Container Registry to fit your project needs.
- [Load VS Code extensions automatically](https://code.visualstudio.com/docs/devcontainers/.containers#_create-a-devcontainerjson-file) under `customizations -> vscode -> extensions`.
- Use [lifecycle commands](https://containers.dev/implementors/json_reference/#lifecycle-scripts) to load assets, run automations, and more.
- The `./.devcontainer/examples/` folder contains examples of development container setups for different languages.

See the Devcontainer reference for a full breakdown of available functions and features: https://containers.dev/implementors/json_reference/

### VS Code settings

The template has preconfigured VS Code and Codespaces settings for visual consistency. 

You are free to _add to_ these settings as long as you don't modify those already present.

`./.vscode/settings.json` is the workspace project settings file for VS Code and Codespaces and it overrides system and user settings. This is what ensures a consistent experience between what you record in your course and what the learner sees in their own Codespace. Changes in this file take effect immediately.

See the VS Code documentation for a full breakdown of how to configure user and workspace settings: https://code.visualstudio.com/docs/configure/settings 

### GitHub settings (Do Not Modify)

The `./.github/` folder contains various files related to GitHub functionality and automation. Leave this folder alone unless your course is specifically covering how to configure these files.

### `.gitignore`

The template comes with a bare-bones `.gitignore` file. Please update this file to fit the needs of your project.

### Legal files (CONTRIBUTING.md, LICENSE, NOTICE)

The template contains three files describing the legal governance of any repository built from it.

- `CONTRIBUTING.md` (Do Not Modify) describes how external contributions to the repository will be handled.
- `LICENSE` (Do Not Modify) provides the text for the LinkedIn Learning Exercise Files License Agreement
- `NOTICE` extends `LICENSE` to address 3rd party dependencies and needs to be updated if your project includes open source packages and/or dependencies. See separate documentation on how to update the `NOTICE` file.


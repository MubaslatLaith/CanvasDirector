# CanvasDirector

CanvasDirector is an agentic image generation and editing framework built around InvokeAI. It combines:

- InvokeAI API and frontend automation (through a bridge) for image generation, inpainting, canvas operations, and reference image management.
- LLM-based agents for planning, execution, critique, and workflow orchestration.
- Perception tools (currently SAM3 segmentation) exposed through FastAPI services.
- Workspace management for coordinating generation jobs, reference images, and editing workflows.

The long-term goal is to create a context-aware image generation system capable of planning, executing, evaluating, and refining image editing tasks autonomously.

---

# Installation

Clone the repository and run the setup script:

```bash
git clone https://github.com/MubaslatLaith/ContextManagerV3.git
cd ContextManagerV3
bash setup.sh
```

---

# Runtime Components

The system requires several services running simultaneously.

## 1. InvokeAI

Start InvokeAI in a dedicated terminal or screen session.

```bash
source invokeai/.venv/bin/activate
invokeai-web --root /workspace/invokeai
```


---

## 2. LLM Service

Run a local LLM in a separate terminal or screen session.

Examples:

```bash
bash deploy_qwen_3.5_9b_q8.sh
```

or

```bash
bash deploy_qwen_3.6_27b_q3.sh
```

Different LLMs can be used depending on the task. Thinking/non-thinking behavior, tool-calling settings, prompts, and generation parameters should be tuned per workflow.

---

## 3. Perception / Additional Generation Tools Service

Start the FastAPI service that exposes additional perception and generation tools.

Currently implemented:

- SAM3 segmentation

```bash
source .venv/bin/activate
python tools_app.py
```

---

## 4. CanvasDirector

Activate the main CanvasDirector environment:

```bash
source .venv/bin/activate
```

The test suites can then be used to interact with the various components of the system.

---

# Test Directories

## test_agents

Examples and experiments for agent implementations.

Includes different agent roles used throughout CanvasDirector:

- Planner agents
- Executor agents
- Critic agents (Task specific and Overall Image Quality) 
- QA agents


---

## test_scripts

Examples demonstrating interaction with InvokeAI through:

- The InvokeAI REST API client
- The UI bridge

The bridge implementation can be found in the companion repository:

https://github.com/MubaslatLaith/InvokeAI-ContextManager

These examples cover functionality such as:

- Workspace initialization
- Text-to-image generation
- Inpainting
- Reference image management
- Canvas operations (e.g., reset canvas, and mask, ref, raster image assignment)

---

## test_perception_tools

Examples for perception-related tooling.

Currently includes:

- SAM3 image segmentation

---

## test_generation_tools

Examples demonstrating workspace management and multi-agent workflows.

Includes:

- Agent interactions
- Generation pipelines
- Context management workflows
- Workspace state management

---

# Current Capabilities

## Image Generation

- Text-to-image generation
- Reference-guided generation
- Inpainting workflows

## Workspace Management

- Board creation and management
- Image uploads
- Reference image handling
- Canvas management

## Agent Framework

- Planner agents
- Executor agents
- Critic agents
- QA agents

## Perception

- SAM3 segmentation

---

# Architecture Overview

```text
                +------------------+
                |      User        |
                +--------+---------+
                         |
                         v
                +------------------+
                |   CanvasDirector |
                +--------+---------+
                         |
          +--------------+--------------+
          |                             |
          v                             v
 +------------------+        +------------------+
 |      Agents      |        | Perception Tools |
 | Planner/Critic   |        |      SAM3        |
 | Executor/QA      |        +------------------+
 +--------+---------+
          |
          v
 +------------------+
 |     InvokeAI     |
 | API + UI Bridge  |
 +------------------+
```

---

# Project Vision

Current image generation systems typically operate as single-shot tools. CanvasDirector aims to introduce a persistent reasoning layer capable of:

- Understanding user goals.
- Planning multi-step image generation and editing workflows.
- Selecting appropriate generation strategies.
- Using perception tools to localize and analyze image issues.
- Managing reference images and workspace state.
- Critiquing outputs and iteratively refining results.

Future work includes:

- Additional perception models (depth, pose, etc.).
- Expanded editing workflows.
- Strategy selection and automatic retries.
- Learning from successful and unsuccessful generation attempts.
- Improved agent coordination and workspace memory.
- Evaluate and compare different agent managment strategies

---

# Notes

- InvokeAI, the LLM service, and the tools FastAPI server must all be running before executing most workflows.
- The current implementation uses Qwen models, but other LLMs can be substituted.
- Additional perception and generation tools can be added through the FastAPI tools service.
- The project is actively evolving toward a fully agentic image generation and editing system.

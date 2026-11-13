# 🤖 Robotics Fundamentals

A collection of Python exercises exploring the mathematics behind robotics, developed as part of my undergraduate learning in Computer Engineering.

This repository documents my progress in understanding how robots represent orientation, transform coordinates, and describe motion through practical numerical examples.

## 🎯 Learning Goals

- Connect robotics theory with working Python code.
- Understand the geometry behind rotation matrices and coordinate transformations.
- Verify mathematical properties through numerical calculations.
- Build a foundation for studying robot kinematics.

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python** | Implementing mathematical concepts and exercises |
| **NumPy** | Matrix operations, numerical calculations, and linear algebra |

## 📁 Repository Structure

The repository is organized into topic-based folders. Each folder contains its own README with relevant theory, explanations, and instructions for running the examples.

```text
Robotics-Fundamentals/
│
├── README.md
├── requirements.txt
│
└── 01-rotation-matrices/
    ├── README.md
    └── Python exercise scripts
```

## 📚 Topics & Exercises

Each topic introduces a specific mathematical concept used in robotics, supported by practical Python implementations.

| Topic | Key Concepts | Status |
|---|---|---|
| [Rotation Matrices](01-rotation-matrices/) | 3D orientation representation, matrix operations, orthogonality, and preservation of handedness | Implemented |

Additional topics will be added as my learning progresses.

## 🚀 Getting Started

### 1. Set up the environment

Install Python and clone or download this repository.

### 2. Install dependencies

Open a terminal in the repository's root directory and run:

```bash
python -m pip install -r requirements.txt
```

### 3. Explore the exercises

Navigate to the relevant topic folder and follow its README for explanations and execution instructions.

Run the Python scripts using:

```bash
python <script_name>.py
```

### 4. Verify NumPy installation

You can check whether NumPy is installed by running:

```bash
python -c "import numpy; print(numpy.__version__)"
```

## 🧠 Suggested Learning Workflow

For each topic, the exercises are intended to be explored in the following order:

1. **Understand the theory** – Read the topic's README and review the mathematical concepts.
2. **Explore the implementation** – Examine how the concepts are represented using Python and NumPy.
3. **Run the examples** – Execute the scripts and observe the numerical outputs.
4. **Experiment** – Modify values and test how the results change.

## 📝 Learning Notes

These exercises are intended for learning and experimentation. Comments and explanations capture the reasoning behind the calculations, alongside the code itself.

References and credits for examples adapted from lectures, textbooks, or tutorials are included in the relevant topic folders.

---

*This repository is a continuous learning project. New topics, implementations, and mathematical explorations will be added as I progress through robotics fundamentals.*

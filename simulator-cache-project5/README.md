# Pipelined Hack CPU Simulator & HDL

A pipelined implementation of the Hack computer architecture (inspired by _Nand2Tetris_), featuring a Python behavioral model, hazard detection, data forwarding logic, and hardware description language (HDL) skeletons.

---

## Project Context (Proje 5 — CPU & Computer Architecture)

- **Current Components:** CPU, Memory, Computer.
- **Pipeline Extension:** The original Hack CPU operates in a single clock cycle. This project models a fetch → decode → execute pipeline in Python and HDL, managing hazard situations (data hazards, control hazards). This work serves as direct preparation for advanced computer architecture courses (such as CPEN 411).

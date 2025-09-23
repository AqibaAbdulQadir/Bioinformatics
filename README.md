# DNA Sequence Alignment Visualizer :)

This project contains Python code to visualize two classic dynamic programming algorithms for DNA sequence alignment: **Needleman-Wunsch** and **Smith-Waterman**. It computes the scoring matrix for two given DNA sequences and generates a heatmap with arrows to show all possible optimal paths. I just came from uni after studying it in today's class and felt like bringing it to life.

## Features

  * **Needleman-Wunsch Algorithm:** Implements a global sequence alignment algorithm. The visualization shows the scoring matrix and the optimal path(s) that align the full sequences.
  * **Smith-Waterman Algorithm:** Implements a local sequence alignment algorithm. The visualization highlights the highest-scoring local alignment(s) within the sequences.
  * **Dynamic Visualization:** Generates a heatmap of the scoring matrix and overlays it with arrows indicating the optimal path(s) for the alignment.
  * **Interactive Command Line Interface:** Allows the user to input two DNA sequences and choose the desired algorithm directly from the terminal.
  * **Modular Code:** The logic for the dynamic programming functions is separated from the visualization code, making it easy to understand and extend. You can also use this code to understand how it really works and tweak it as you like.

## Getting Started

### Prerequisites

To run this code, you'll need the following Python libraries:

  * `numpy`
  * `matplotlib`

You can install them using `pip`:

```bash
pip install numpy matplotlib
```

### Usage

The program is run from the command line and prompts the user for input.

1.  Make sure all the Python files (`visualise_dp.py`, `dynamic_programming.py`, `process_dp.py`) are in the same directory.
2.  Run the main script from your terminal:

<!-- end list -->

```bash
python visualise_dp.py
```

3.  Follow the on-screen prompts to enter your DNA sequences and select an algorithm. The program will then display a visualization of the alignment matrix.

**Example Input:**

  * **Enter first sequence A:** `CAGGTAGTG`
  * **Enter second sequence B:** `CTAGTAG`
  * **Enter algorithm number:** `1` (for Needleman Wunsch)
  * **Enter Sequence Type:** `1` (for DNA)
  </br></br>
  ![terminal.png](images%2Fterminal.png)
The program will then generate a plot like so:
![graph.png](images%2Fgraph.png)
## Code Structure
  * `visualise_dp.py`: Main script that handles user input and calls the other modules to run the alignment and visualization
  * `dynamicrporgramming.py`: Contains the core dynamic programming functions (`dna_needle_man`, `dna_water_man`) and the general `dp_func` that builds the scoring matrix. I'll add more as we study further for protein sequences as well.
  * `process_dp.py`: Handles all the visualization logic. It converts the scoring matrix to a plottable format and uses `matplotlib` to create the heatmap and path arrows.
  
## Author

  * **Aqiba Abdul Qadir** - Just felt like having fun :)

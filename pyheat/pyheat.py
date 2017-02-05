# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""Class and Method definitions to view python file as a heatmap highlighting
   the most time consuming parts of the file.

   Usage:

   To get help: `python pyheat.py --help`
   For heatmap: `python pyheat.py --pyfile <filename>`
"""
import argparse

import matplotlib.pyplot as plt
import numpy as np
import pprofile

__author__ = 'Vishwas B Sharma'
__author_email__ = 'sharma.vishwas88@gmail.com'
__version__ = '0.0.1'


class PyHeat(object):
    """Class to display the python file provided as a heatmap highlighting the
       most time consuming parts of the file.
    """

    class FileDetails(object):
        """Class to keep track of useful file related details used in creating
           heatmaps.
        """

        def __init__(self, filepath):
            """Constructor.

               @param filepath: Path of the file to profile.
            """
            self.path = filepath
            self.lines = []
            self.length = 0
            self.data = None

    def __init__(self, filepath):
        """Constructor.

           @param filepath: Path of the file to profile.
        """
        self.pyfile = PyHeat.FileDetails(filepath)
        self.line_profiler = None

    def create_heatmap(self):
        """Method to define the heatmap using profile data."""
        # Profile the file.
        self.__profile_file()
        # Map profile stats to heatmap data.
        self.__fetch_heatmap_data_from_profile()
        # Create heatmap.
        self.__create_heatmap_plot()

    def show_heatmap(self):
        """Method to actually display the heatmap created."""
        plt.show()

    def __profile_file(self):
        """Method used to profile the given file line by line."""
        self.line_profiler = pprofile.Profile()
        self.line_profiler.runfile(
            open(self.pyfile.path, 'r'), {}, self.pyfile.path)

    def __get_line_profile_data(self):
        """Method to procure line profiles.

           @return: Line profiles if the file has been profiles else empty
           dictionary.
        """
        if self.line_profiler is None:
            return {}
        return self.line_profiler.file_dict[self.pyfile.path].line_dict

    def __fetch_heatmap_data_from_profile(self):
        """Method to create heatmap data from profile information."""
        # Read lines from file.
        with open(self.pyfile.path, 'r') as file_to_read:
            for line in file_to_read:
                # Remove return char from the end of the line and add a
                # space in the beginning for better visibility.
                self.pyfile.lines.append('  ' + line.strip('\n'))

        # Total number of lines in file.
        self.pyfile.length = len(self.pyfile.lines)

        # Fetch line profiles.
        line_profiles = self.__get_line_profile_data()

        # Creating an array of data points. As the profile keys are 1 indexed
        # we should range from 1 to line_count + 1 and not 0 to line_count.
        arr = []
        for line_num in range(1, self.pyfile.length + 1):
            if line_num in line_profiles:
                arr.append([line_profiles[line_num][-1]])
            else:
                arr.append([0.0])

        # Create nd-array from list of data points.
        self.pyfile.data = np.array(arr)

    def __create_heatmap_plot(self):
        """Method to actually create the heatmap from profile stats."""
        # Define the heatmap plot.
        _, ax = plt.subplots()
        heatmap = ax.pcolor(self.pyfile.data, cmap='OrRd')

        # X Axis
        # Remove X axis.
        ax.xaxis.set_visible(False)

        # Y Axis
        # Create lables for y-axis ticks
        row_labels = range(1, self.pyfile.length + 1)
        # Set y-tick labels.
        ax.set_yticklabels(row_labels, minor=False)
        # Put y-axis major ticks at the middle of each cell.
        ax.set_yticks(np.arange(self.pyfile.data.shape[0]) + 0.5, minor=False)
        # Inver y-axis to have top down line numbers
        ax.invert_yaxis()

        # Plot definitions
        # Set plot y-axis label.
        plt.ylabel("Line Number")
        # Annotate each cell with lines in file in order.
        for i, line in enumerate(self.pyfile.lines):
            plt.text(0.0, i + 0.5, line, ha='left', va='center')

        # Define legend
        cbar = plt.colorbar(heatmap)
        cbar.set_label('# of seconds')


def main():
    """Starting point for the program execution."""
    # Create command line parser.
    parser = argparse.ArgumentParser()
    # Adding command line arguments.
    parser.add_argument('--pyfile', help='File to be profiled.', default=None)
    # Parse command line arguments.
    arguments = parser.parse_args()

    # Core functionality.
    pyheat = PyHeat(arguments.pyfile)
    pyheat.create_heatmap()
    pyheat.show_heatmap()


if __name__ == '__main__':
    main()

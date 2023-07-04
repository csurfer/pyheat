# -*- coding: utf-8 -*-
"""
pyheat.pyheat
~~~~~~~~~~~

Class definitions to view python file as a heatmap highlighting
the most time consuming parts of the file.
"""

import matplotlib.pyplot as plt
import numpy as np
import pprofile
from matplotlib.widgets import Slider


class PyHeat(object):
    """Class to display the python file provided as a heatmap highlighting the
    most time consuming parts of the file.
    """

    class FileDetails(object):
        """Class to keep track of useful file related details used in creating
        heatmaps.
        """

        def __init__(self, filepath, argv):
            """Constructor.

            @param filepath: Path of the file to profile.
            """
            self.path = filepath
            self.lines = []
            self.length = 0
            self.data = None
            self.argv = [filepath] + argv

    def __init__(self, filepath, argv):
        """Constructor.

        @param filepath: Path of the file to profile.
        """
        self.pyfile = PyHeat.FileDetails(filepath, argv)
        self.line_profiler = None

    def create_heatmap(self):
        """Method to define the heatmap using profile data."""
        # Profile the file.
        self.__profile_file()
        # Map profile stats to heatmap data.
        self.__fetch_heatmap_data_from_profile()
        # Create heatmap.
        self.__create_heatmap_plot()

    def show_heatmap(self, blocking=True, output_file=None, enable_scroll=False):
        """Method to actually display the heatmap created.

        @param blocking: When set to False makes an unblocking plot show.
        @param output_file: If not None the heatmap image is output to this
        file. Supported formats: (eps, pdf, pgf, png, ps, raw, rgba, svg,
        svgz)
        @param enable_scroll: Flag used add a scroll bar to scroll long files.
        """
        if output_file is None:
            if enable_scroll:
                # Add a new axes which will be used as scroll bar.
                axpos = plt.axes([0.12, 0.1, 0.625, 0.03])
                spos = Slider(axpos, 'Scroll', 10, len(self.pyfile.lines))

                def update(val):
                    """Method to update position when slider is moved."""
                    pos = spos.val
                    self.ax.axis([0, 1, pos, pos - 10])
                    self.fig.canvas.draw_idle()

                spos.on_changed(update)
            plt.show(block=blocking)
        else:
            plt.savefig(output_file)

    def close_heatmap(self):
        """Method to close the heatmap display created."""
        plt.close('all')

    def __profile_file(self):
        """Method used to profile the given file line by line."""
        self.line_profiler = pprofile.Profile()
        self.line_profiler.runfile(open(self.pyfile.path, 'r'), self.pyfile.argv, self.pyfile.path)

    def __get_line_profile_data(self):
        """Method to procure line profiles.

        @return: Line profiles if the file has been profiles else empty
        dictionary.
        """
        if self.line_profiler is None:
            return {}

        # the [0] is because pprofile.Profile.file_dict stores the line_dict
        # in a list so that it can be modified in a thread-safe way
        # see https://github.com/vpelletier/pprofile/blob/da3d60a1b59a061a0e2113bf768b7cb4bf002ccb/pprofile.py#L398
        return self.line_profiler.file_dict[self.pyfile.path][0].line_dict

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
                # line_profiles[i] will have multiple entries if line i is
                # invoked from multiple places in the code. Here we sum over
                # each invocation to get the total time spent on that line.
                line_times = [ltime for _, ltime in line_profiles[line_num].values()]
                arr.append([sum(line_times)])
            else:
                arr.append([0.0])

        # Create nd-array from list of data points.
        self.pyfile.data = np.array(arr)

    def __create_heatmap_plot(self):
        """Method to actually create the heatmap from profile stats."""
        # Define the heatmap plot.
        height = len(self.pyfile.lines) / 3
        width = max(map(lambda x: len(x), self.pyfile.lines)) / 8
        self.fig, self.ax = plt.subplots(figsize=(width, height))

        # Set second sub plot to occupy bottom 20%
        plt.subplots_adjust(bottom=0.20)

        # Heat scale orange to red
        heatmap = self.ax.pcolor(self.pyfile.data, cmap='OrRd')

        # X Axis
        # Remove X axis.
        self.ax.xaxis.set_visible(False)

        # Y Axis
        # Create lables for y-axis ticks
        row_labels = range(1, self.pyfile.length + 1)
        # Put y-axis major ticks at the middle of each cell.
        self.ax.set_yticks(np.arange(self.pyfile.data.shape[0]) + 0.5, minor=False)
        # Set y-tick labels.
        self.ax.set_yticklabels(row_labels, minor=False)
        # Inver y-axis to have top down line numbers
        self.ax.invert_yaxis()

        # Plot definitions
        # Set plot y-axis label.
        plt.ylabel('Line Number')
        # Annotate each cell with lines in file in order.
        max_time_spent_on_a_line = max(self.pyfile.data)
        for i, line in enumerate(self.pyfile.lines):
            # In order to ensure easy readability of the code, we need to
            # invert colour of text display for darker colours which
            # correspond to higher amount of time spent on the line.
            if self.pyfile.data[i] >= 0.7 * max_time_spent_on_a_line:
                color = (1.0, 1.0, 1.0)  # White text
            else:
                color = (0.0, 0.0, 0.0)  # Black text
            plt.text(
                0.0,
                i + 0.5,
                line,
                ha='left',
                va='center',
                color=color,
                clip_on=True,
            )

        # Define legend
        cbar = plt.colorbar(heatmap)
        cbar.set_label('# of seconds')

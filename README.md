# Face Recognition Attendance System

This is a Python-based face recognition attendance system that uses OpenCV and face_recognition library to recognize faces in a live video stream, track attendance, and log attendance records in a CSV file. The system allows for real-time recognition of known individuals and keeps track of their attendance automatically.

## Features

- Real-time face recognition using webcam or video input.
- Automatic attendance tracking for recognized individuals.
- Logging of attendance records in a CSV file with timestamps.
- Customizable face recognition threshold for accuracy control.
- Support for multiple known individuals with customizable names.

## Setup and Dependencies

1. **Install Python dependencies**: Ensure you have Python installed on your system. Install the required Python libraries using the following command:

   ```
   pip install opencv-python face_recognition numpy cmake (cmake is ued for managing the build process for C/C++ code/components of face_recognition library).
   ```

2. **Configure known individuals**: Update the code to specify the image paths and names of known individuals for face recognition.

3. **Run the script**: Execute the script `attendance_system.py` to start the face recognition attendance system.
4. **Build Tools**: If you are using VS Code, make sure you have installed VS Code Community version for build tools(C++)(to compile face_recognition library).

## Usage

1. Run the script `attendance_system.py` using Python.
2. Ensure that your webcam or video input device is properly configured and connected.
3. The system will start recognizing faces in the video stream and display their names if they are known individuals.
4. If a recognized individual is present, their attendance will be logged in real-time in a CSV file with timestamps.
5. Press `q` to exit the application and stop the face recognition process.

## Files

- **attendance_system.py**: Main script for the face recognition attendance system.
- **README.md**: Documentation for the project.
- **requirements.txt**: List of Python dependencies.
- **.gitignore**: Specifies files to be ignored by version control.
- **LICENSE**: License information for the project.

## Dependencies

- OpenCV: Library for computer vision tasks.
- face_recognition: Library for face recognition tasks.
- numpy: Library for numerical computations.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or feature requests, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

FROM osrf/ros:jazzy-desktop

# User setup
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create user with sudo privileges
RUN if ! id -u $USER_UID >/dev/null 2>&1; then \
    groupadd --gid $USER_GID $USERNAME && \
    useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME; \
    fi

# Add sudo support
RUN apt update && \
    apt install -y sudo && \
    echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to non-root user
USER $USERNAME

# Add user to video group to allow access to webcam
RUN sudo usermod --append --groups video $USERNAME

# Update all packages
RUN sudo apt update && sudo apt upgrade -y

# Install Git
RUN sudo apt install -y git

# Update rosdep
RUN rosdep update

# Configure ROS env for non-root user
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

################################
##        CUSTOM SETUP        ##
################################
# Update and install packages
RUN sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-poetry

# Add alias for Python
RUN echo "alias python=python3" >> ~/.bashrc

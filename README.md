# Smart Device Management System

A Python implementation of a smart device management system that allows tracking and controlling various IoT devices.

## Overview

The `SmartDevice` class provides a foundation for managing smart devices with features like status tracking, online state management, and device information retrieval.

## Features

### Core Functionality
- Device creation with name, model number, and online status
- Status attribute management
- Online state toggling
- Device reset capability
- Device information retrieval
- Automatic device counting

### SmartDevice Class Methods

#### Basic Methods
- `__init__(device_name, model_number, is_online=False)`: Initialize a new device
- `update_status(attribute, value)`: Add or update device status attributes
- `get_status(attribute)`: Retrieve specific status attributes
- `toggle_online()`: Switch device online state
- `reset()`: Clear all status attributes
- `device_info()`: Get complete device information
- `__call__()`: Return formatted device string


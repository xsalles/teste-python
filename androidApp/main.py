# main.py
import os
import threading
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

"""
Module that provides Android permissions functionality
- For development: provides dummy implementations
- On Android: imports real implementations
"""
from kivy.utils import platform

if platform == 'android':
    try:
        # Real Android implementation when running on Android device
        from android.permissions import request_permissions as _request_permissions
        from android.permissions import Permission as _Permission
        
        request_permissions = _request_permissions
        Permission = _Permission
    except ImportError:
        # Fallback if android.permissions is not available
        def request_permissions(permissions):
            print(f"Would request permissions: {permissions}")
        
        class Permission:
            INTERNET = "android.permission.INTERNET"
            READ_EXTERNAL_STORAGE = "android.permission.READ_EXTERNAL_STORAGE"
            WRITE_EXTERNAL_STORAGE = "android.permission.WRITE_EXTERNAL_STORAGE"
else:
    # Dummy implementation for development/testing on non-Android platforms
    def request_permissions(permissions):
        print(f"Would request permissions: {permissions}")
    
    class Permission:
        INTERNET = "android.permission.INTERNET"
        READ_EXTERNAL_STORAGE = "android.permission.READ_EXTERNAL_STORAGE"
        WRITE_EXTERNAL_STORAGE = "android.permission.WRITE_EXTERNAL_STORAGE"

# Import your data collection function
from collect_and_send_data import collect_and_send_data

class DeviceCollectorApp(App):
    def build(self):
        # Create a simple layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add app title
        title = Label(
            text='Device Data Collector',
            font_size=24,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        # Add description
        description = Label(
            text='This app collects device information and sends it to a server.',
            text_size=(400, None),
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(description)
        
        # Status label to show results
        self.status_label = Label(
            text='Ready to collect data',
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.status_label)
        
        # Button to trigger data collection
        collect_button = Button(
            text='Collect and Send Data',
            size_hint_y=None,
            height=50
        )
        collect_button.bind(on_press=self.start_collection)
        layout.add_widget(collect_button)
        
        # Schedule periodic collection (every 2 hours)
        Clock.schedule_once(self.request_permissions, 1)
        Clock.schedule_once(self.start_periodic_collection, 5)
        
        return layout
    
    def request_permissions(self, dt):
        if platform == 'android':
            request_permissions([
                Permission.INTERNET,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE
            ])
    
    def start_collection(self, instance):
        """Trigger data collection when button is pressed"""
        self.status_label.text = 'Collecting data...'
        threading.Thread(target=self.collect_data).start()
    
    def collect_data(self):
        """Run the data collection in a separate thread"""
        try:
            server_url = "https://your-server-url.com/device/android"  # Replace with your actual server URL
            result = collect_and_send_data(server_url)
            
            # Update UI from main thread
            Clock.schedule_once(lambda dt: self.update_status(result), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_status(False, str(e)), 0)
    
    def update_status(self, success, error=None):
        """Update the status label with the result"""
        if success:
            self.status_label.text = 'Data collected and sent successfully!'
        else:
            self.status_label.text = f'Error: {error if error else "Failed to send data"}'
    
    def start_periodic_collection(self, dt):
        """Start periodic data collection (every 2 hours)"""
        def periodic_collection():
            while True:
                self.collect_data()
                # Sleep for 2 hours (in seconds)
                time.sleep(2 * 60 * 60)
        
        # Start the periodic collection in a background thread
        threading.Thread(target=periodic_collection, daemon=True).start()

if __name__ == '__main__':
    DeviceCollectorApp().run()
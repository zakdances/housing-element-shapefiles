from typing import TypedDict, List, Optional, Literal

class AttendeeInfo(TypedDict):
    name: str
    is_vip: bool

class EventManager:
    EventStatus = Literal["ACTIVE", "CANCELLED", "VIP_EXCLUSIVE"]

    def __init__(self, event_name: str, max_capacity: int, vip_only: bool = False) -> None:
        if max_capacity <= 0:
            raise ValueError("Max capacity must be greater than 0")
        
        self.event_name: str = event_name
        self.max_capacity: int = max_capacity
        self.vip_only: bool = vip_only
        self.attendees: List[AttendeeInfo] = []
        self.status: EventManager.EventStatus = "ACTIVE"

    def _calculate_vip_percentage(self) -> float:
        """Calculate the percentage of VIP attendees"""
        if not self.attendees:
            return 0.0
        vip_count = self.get_vip_count()
        return (vip_count / len(self.attendees)) * 100

    def _update_event_status(self) -> None:
        """Update event status based on current attendees"""
        if len(self.attendees) == 0:
            self.status = "CANCELLED"
            return

        vip_percentage = self._calculate_vip_percentage()
        if vip_percentage > 75:
            self.status = "VIP_EXCLUSIVE"
        else:
            self.status = "ACTIVE"

    def register_attendee(self, name: str, is_vip: bool = False) -> str:
        if self.status == "CANCELLED":
            return "Cannot register: Event is cancelled"
        
        if self.status == "VIP_EXCLUSIVE":
            return "Cannot register: Event has become VIP exclusive due to high VIP attendance"

        if self.vip_only and not is_vip:
            return "Registration failed: This is a VIP-only event"

        if len(self.attendees) >= self.max_capacity:
            return "Registration failed: Event is at maximum capacity"

        if any(attendee["name"] == name for attendee in self.attendees):
            return f"Registration failed: {name} is already registered"

        self.attendees.append({"name": name, "is_vip": is_vip})
        self._update_event_status()  # Check status after adding
        return f"{name} successfully registered for {self.event_name}"

    def remove_attendee(self, name: str) -> str:
        attendee_index: Optional[int] = None
        for i, attendee in enumerate(self.attendees):
            if attendee["name"] == name:
                attendee_index = i
                break

        if attendee_index is not None:
            self.attendees.pop(attendee_index)
            self._update_event_status()  # Check status after removal
            return f"{name} successfully removed from {self.event_name}"
        return f"Removal failed: {name} is not registered for this event"

    def list_attendees(self) -> str:
        if self.status == "CANCELLED":
            return "Event is cancelled - no attendees"

        if not self.attendees:
            return "No attendees registered"

        result: List[str] = [
            f"\nAttendees for {self.event_name} ({self.status}):",
            "-" * 40
        ]
        
        for attendee in self.attendees:
            vip_status = "VIP" if attendee["is_vip"] else "Regular"
            result.append(f"{attendee['name']} - {vip_status}")

        vip_percentage = self._calculate_vip_percentage()
        result.append(f"\nTotal attendees: {len(self.attendees)}/{self.max_capacity}")
        result.append(f"VIP percentage: {vip_percentage:.1f}%")
        return "\n".join(result)

    def get_event_info(self) -> str:
        access_type = "VIP Only" if self.vip_only else "Open to All"
        vip_percentage = self._calculate_vip_percentage()
        return (
            f"Event: {self.event_name}\n"
            f"Status: {self.status}\n"
            f"Access: {access_type}\n"
            f"Capacity: {len(self.attendees)}/{self.max_capacity}\n"
            f"VIP percentage: {vip_percentage:.1f}%"
        )

    def get_vip_count(self) -> int:
        return sum(1 for attendee in self.attendees if attendee["is_vip"])


# Updated example usage
def main() -> None:
    try:
        # Create an event with max capacity of 4
        event = EventManager("Concert Night", 4, vip_only=False)

        # Register attendees to trigger VIP_EXCLUSIVE
        print(event.register_attendee("Alice", is_vip=True))    # VIP 1
        print(event.register_attendee("Bob", is_vip=True))      # VIP 2
        print(event.register_attendee("Charlie", is_vip=True))  # VIP 3
        print(event.register_attendee("David", is_vip=False))   # Regular 1
        # Now VIP percentage = 75%, next registration should be blocked

        print("\n" + event.list_attendees())
        print("\n" + event.get_event_info())

        # Try to register new attendee (should fail due to VIP_EXCLUSIVE)
        print("\n" + event.register_attendee("Eve", is_vip=True))

        # Remove a VIP to drop below 75%
        print("\n" + event.remove_attendee("Alice"))
        print(event.list_attendees())

        # Should now allow registration
        print("\n" + event.register_attendee("Eve", is_vip=False))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
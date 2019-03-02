class StudyRoom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity

    def __str__(self):
        formatted_number = self.room_number
        if formatted_number < 10:
            formatted_number = '0' + str(formatted_number)
        return 'Room {room_number} (Capacity {capacity})'.format(room_number=formatted_number, capacity=self.capacity)
    
    def __repr__(self):
        return 'StudyRoom(room_number: {room_number}, capacity: {capacity})'.format(room_number=self.room_number, capacity=self.capacity)
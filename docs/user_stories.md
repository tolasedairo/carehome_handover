# Care Home Handover App - User Stories

---

## **Manager**

### User Story
As a **Manager**, I want to oversee all residents and carers and ensure handovers are complete so that continuity of care is maintained.

### Acceptance Criteria
- Can log in and out securely  
- Can view all residents’ full handover information  
- Can mark handovers as reviewed  

### Tasks
- Implement login/logout functionality  
- Create a dashboard to view all residents and carers  
- Add handover review and marking system  
- Assign permissions for full access  

---

## **Senior Carer**

### User Story
As a **Senior Carer**, I want to record detailed handover information and supervise carers so that critical resident information is not missed.

### Acceptance Criteria
- Can access full resident details  
- Can create and update handover notes  
- Can view which carers have acknowledged reading handovers  

### Tasks
- Implement handover creation and update forms  
- Display full resident info for senior carers  
- Track and display acknowledgements from carers  
- Ensure role-based access is enforced  

---

## **Carer**

### User Story
As a **Carer**, I want to access essential information for residents on my shift so that I can provide proper care without seeing sensitive details I don’t need.

### Acceptance Criteria
- Can view only essential handover information  
- Can acknowledge that they have read the handover  

### Tasks
- Implement filtered handover view for carers  
- Add acknowledgement button/functionality  
- Ensure restricted access to sensitive data  

---

## **All Users**

### User Story
As **any user of the system**, I want to log in securely so that sensitive information is protected and only authorized users can access the app.

### Acceptance Criteria
- Login is required for all features  
- Role-based permissions are enforced  
- Session and account security implemented  

### Tasks
- Implement authentication for all users  
- Enforce role-based access control  
- Set up secure session handling and password policies  

---

## **Handover System**

### User Story
As the **Handover System**, I want to ensure continuity of care so that critical information is passed between shifts without errors.

### Acceptance Criteria
- Notes are timestamped  
- Senior carers add detailed notes; carers see filtered info  

### Tasks
- Create timestamped handover notes  
- Filter handover info based on user role  
- Store handover history for auditing  

---

## **Optional Features (Future)**

### User Story
As a **Manager**, I want notifications and an audit trail so that I can improve efficiency and traceability.

### Acceptance Criteria
- Notifications for unread handovers  
- Audit trail of activity available  

### Tasks
- Implement notification system for unread handovers  
- Create audit trail log for handover actions  
- Restrict audit access to managers  

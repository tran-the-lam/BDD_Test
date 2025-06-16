# Profile Component User Stories

## User Profile Management

### US-028: Xem thông tin cá nhân
**Là** người dùng đã đăng nhập  
**Tôi muốn** xem thông tin cá nhân của mình  
**Để** kiểm tra và quản lý tài khoản  

**Acceptance Criteria:**
- Modal hiển thị thông tin: tên, email, số điện thoại, địa chỉ
- Hiển thị ngày tham gia (Member Since)
- Tab interface để chuyển đổi giữa Profile và Order History
- Icon tương ứng cho từng loại thông tin

### US-029: Chỉnh sửa thông tin cá nhân
**Là** người dùng đã đăng nhập  
**Tôi muốn** cập nhật thông tin cá nhân  
**Để** giữ thông tin luôn chính xác và mới nhất  

**Acceptance Criteria:**
- Button "Edit" để chuyển sang chế độ chỉnh sửa
- Form fields cho: tên, số điện thoại, địa chỉ
- Email không thể chỉnh sửa (readonly)
- Buttons "Save Changes" và "Cancel"
- Validation cho các trường thông tin

### US-030: Xem lịch sử đơn hàng
**Là** khách hàng đã mua hàng  
**Tôi muốn** xem danh sách đơn hàng đã đặt  
**Để** theo dõi trạng thái và lịch sử mua sắm  

**Acceptance Criteria:**
- Tab "Order History" trong profile modal
- Danh sách đơn hàng hiển thị: mã đơn, ngày đặt, tổng tiền, trạng thái
- Status badge với màu sắc phân biệt: pending, processing, shipped, delivered, cancelled
- Sắp xếp theo ngày đặt hàng (mới nhất trước)

### US-031: Xem chi tiết đơn hàng
**Là** khách hàng  
**Tôi muốn** xem chi tiết một đơn hàng cụ thể  
**Để** biết thông tin đầy đủ về đơn hàng  

**Acceptance Criteria:**
- Button "View Details" cho mỗi đơn hàng
- Hiển thị: danh sách sản phẩm, số lượng, giá
- Thông tin giao hàng: địa chỉ, ngày giao dự kiến/thực tế
- Timeline trạng thái đơn hàng
- Button in hoá đơn (nếu có)

### US-032: Trạng thái đơn hàng với màu sắc
**Là** khách hàng  
**Tôi muốn** phân biệt trạng thái đơn hàng qua màu sắc  
**Để** nhanh chóng nhận biết tình trạng đơn hàng  

**Acceptance Criteria:**
- Pending: màu vàng (yellow)
- Processing: màu xanh dương (blue)
- Shipped: màu tím (purple)
- Delivered: màu xanh lá (green)
- Cancelled: màu đỏ (red)
- Badge design với background và text color tương ứng

### US-033: Empty state cho đơn hàng
**Là** khách hàng mới  
**Tôi muốn** thấy thông báo khi chưa có đơn hàng nào  
**Để** biết cần mua sắm để có lịch sử đơn hàng  

**Acceptance Criteria:**
- Icon package và message "No orders yet"
- Text hướng dẫn "Start shopping to see your orders here"
- Center alignment cho empty state
- Friendly và encouraging tone

### US-034: Modal profile responsive
**Là** người dùng trên mobile  
**Tôi muốn** profile modal hiển thị tốt trên điện thoại  
**Để** có thể quản lý tài khoản mọi lúc mọi nơi  

**Acceptance Criteria:**
- Modal responsive với max-height và scroll
- Touch-friendly tabs và buttons
- Proper spacing cho mobile screens
- Easy close với backdrop click hoặc X button

### US-035: Validation thông tin profile
**Là** người dùng  
**Tôi muốn** có validation khi chỉnh sửa thông tin  
**Để** đảm bảo dữ liệu nhập vào hợp lệ  

**Acceptance Criteria:**
- Required validation cho tên
- Phone number format validation
- Address length validation
- Real-time validation feedback
- Disable save button khi có lỗi

## Components Implemented:
- ProfileModal
- ProfileForm
- OrderHistory
- OrderCard
- OrderDetails
- ProfileTabs

## Integration Points:
- AuthContext: để lấy và cập nhật thông tin user
- Order service: để fetch lịch sử đơn hàng
- Toast notifications: để thông báo khi save thành công
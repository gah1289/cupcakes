// window.onload = function() {
// 	if (window.jQuery) {
// 		// jQuery is loaded
// 		alert('jQuery is working');
// 	}
// 	else {
// 		location.reload();
// 	}
// };

const BASE_URL = 'http://127.0.0.1:5000/api';

async function generateCupcake() {
	return `<div class="card">
    <img src="${cupcake.image}" class="card-img-top" alt="${cupcake.flavor} cupcake">
    <div class="card-body">
      <h5 class="card-title">${cupcake.size.capitalize()} ${cupcake.flavor.capitalize()}</h5>
      <button type="button" class="btn btn-primary btn-sm">Edit</button>
<button type="button" class="btn btn-danger btn-sm">Delete</button>
    </div>
  </div>`;
}

// async function showCupcakeList() {
// 	const resp = await axios.get(`${BASE_URL}/cupcakes`);

// 	print('*******************');
// 	console.log(resp);

// 	for (let data of resp.data.cupcakes) {
// 		let cupcake = $(generateCupcake(data));
// 		console.log(cupcake);
// 		$('#cupcake-list').append(cupcake);
// 	}
// }

$('.delete-btn').click(deleteCupcake);

async function deleteCupcake() {
	const id = $(this).data('id');
	await axios.delete(`/api/cupcakes/${id}`);
	$(this).parent().remove();
}

async function updateCupcake() {
	const id = $(this).data('id');
	await axios.patch(`/api/cupcakes/${id}`);
}

$('#new-cupcake').on('submit', async function(e) {
	evt.preventDefault();

	let rating = $('#form-rating').val();
	let size = $('#form-size').val();
	let image = $('#form-image').val();

	const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
		flavor,
		rating,
		size,
		image
	});

	let newCupcake = $(generateCupcake(newCupcakeResponse.data.cupcake));
	$('#cupcake-list').append(newCupcake);
	$('#new-cupcake').trigger('reset');
});

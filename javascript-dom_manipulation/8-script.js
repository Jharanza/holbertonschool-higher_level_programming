document.addEventListener('DOMContentLoaded', () => {
	const data = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr').then(resp => resp.json());

	data.then(({hello}) => {
		const value = document.querySelector('#hello');
		value.textContent = hello;
	});
});

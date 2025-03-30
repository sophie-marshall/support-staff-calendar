<script lang="ts">
	import SubModal from '$lib/SubModal.svelte';

	let showSubModal: boolean = false;

	function handleRequestSub() {
		showSubModal = !showSubModal;
	}
</script>

<main>
	<p>This is where the calendar will live eventually</p>
	<button
		on:click={handleRequestSub}
		style={showSubModal ? 'background: var(--primary-blue); color: white' : ''}
	>
		REQUEST A SUB
	</button>
	<div class="sub-modal-container" style={showSubModal ? 'display: flex;' : 'display: none;'}>
		<SubModal />
	</div>
</main>

<style>
	button {
		padding: 10px 20px;
		border: 1px solid black;
		color: black;
		cursor: pointer;
		background: transparent;
		font-weight: 400;
	}

	button:hover {
		background: rgba(3, 23, 214, 0.7);
		color: white;
	}

	.sub-modal-container {
		padding-top: 20px;
	}
</style>

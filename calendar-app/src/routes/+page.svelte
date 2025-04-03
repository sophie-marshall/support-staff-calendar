<script lang="ts">
	import SubModal from '$lib/SubModal.svelte';

	let showSubModal: boolean = false;

	function handleRequestSub() {
		showSubModal = !showSubModal;
	}

	function setShowSubModal(value: boolean) {
		showSubModal = value;
	}
</script>

<main>
	<p>This is where the calendar will live eventually</p>
	<button class={showSubModal ? 'selected' : ''} on:click={handleRequestSub}>
		REQUEST A SUB
	</button>
	<div class="sub-modal-container" style={showSubModal ? 'display: flex;' : 'display: none;'}>
		<SubModal {setShowSubModal} />
	</div>
</main>

<style>
	button {
		border-radius: 2px;
		padding: 10px 20px;
		border: 1px solid black;
		color: white;
		cursor: pointer;
		background: black;
		font-weight: 400;
		transition:
			transform 0.2s ease-out,
			box-shadow 0.2s ease-out;
	}

	button:hover {
		transform: translateY(-0.125rem);
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	.sub-modal-container {
		padding-top: 20px;
		width: 550px;
	}

	.selected {
		background: black;
		color: white;
		transform: translateY(-0.125rem);
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
	}
</style>

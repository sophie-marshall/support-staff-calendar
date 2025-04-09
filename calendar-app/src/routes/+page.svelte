<script lang="ts">
	import SubModal from '$lib/SubModal.svelte';
	import Calendar from '$lib/Calendar.svelte';

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
	<button class={showSubModal ? 'request-sub-selected' : ''} on:click={handleRequestSub}>
		REQUEST A SUB
	</button>
	<div class="sub-modal-container" style={showSubModal ? 'display: flex;' : 'display: none;'}>
		<SubModal {setShowSubModal} />
	</div>
	<div class="calendar-container">
		<Calendar />
	</div>
</main>

<style>
	.sub-modal-container {
		padding-top: 20px;
		width: 550px;
	}

	.request-sub-selected {
		background: black;
		color: white;
		transform: translateY(-0.125rem);
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
	}

	.calendar-container {
		display: flex;
		padding-top: 20px;
	}
</style>
